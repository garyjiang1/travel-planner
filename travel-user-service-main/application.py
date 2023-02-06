import json
from datetime import datetime
from flask import Response, session, url_for
from flask_cors import CORS
import os
import random

from middleware import notification as notification, security as security
import requests
from oauthlib.oauth2 import WebApplicationClient
from user_service_resource import UserResource
from user import User

from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

# Create the Flask application object.
# Ned to change this and update the local command
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)
# cors = CORS(app, resources={r'/users_service/*': {'origins': '*'}})

itenerary_url = str(os.environ.get("ITENERARY_URL"))
frontend_url = str(os.environ.get("FRONTEND_URL"))

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

# Google OAuth
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# sns = boto3.client('sns', region_name='us-east-2')
trigger_SNS_request = {"path": "/users_service/create_trip", "method": "POST"}

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


'''
@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403
'''


@app.get("/")
def get_service():
    t = str(datetime.now())
    msg = {
        "Service": "User Service",
        "Description ": "A service to manage user accounts/trips/itineraries",
        "at time": t

    }
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/users_service")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<a class='button' href='/logout'>Logout</a>"
            .format(
                current_user.name, current_user.email
            )
        )

    else:
        return '<a class="button" href="/users_service/login2">Google Login</a>'



@app.route("/users_service/recommend", methods=["GET"])
def recommend():
    if request.method == 'GET':
        random_from_location = ["prague", "delhi", "miami"]
        random_to_location = ["california", "dhaka", "milan"]
        random_index_from = random.randint(0,len(random_from_location)-1)
        random_index_to = random.randint(0,len(random_to_location)-1)


        fromLocation = random_from_location[random_index_from]
        toLocation = random_to_location[random_index_to]
        fromDate = "2023-01-08"
        toDate = "2023-01-14"

        # get src airport code
        getAirportCodeUrl = itenerary_url + '/api/flight/' \
                            + fromLocation
        response = requests.request('GET', getAirportCodeUrl)
        response = response.json()
        fromAirport = response[0]['code']

        # get dest airport code
        getAirportCodeUrl = itenerary_url + '/api/flight/' + toLocation
        response = requests.request('GET', getAirportCodeUrl)
        response = response.json()
        toAirport = response[0]['code']

        # call to get flight details from origin to destination
        toFlightDetails = str(
            itenerary_url + '/api/flight?origin=' + fromAirport + '&destination=' + toAirport + '&date=' + fromDate)
        response = requests.request('GET', toFlightDetails)
        toFlightDetails = response.json()
        to_flight_list = []
        for f in toFlightDetails:
            toFlight = {
                "flight_id": f['id'],
                "price": f['price']['amount'],
                "origin_airport": f['legs'][0]['origin']['name'],
                "destination_airport": f['legs'][0]['destination']['name'],
                "departure": f['legs'][0]['departure'],
                "arrival": f['legs'][0]['arrival'],
                "duration": f['legs'][0]['duration'],
                "carrier": f['legs'][0]['carriers'][0]['name'],
            }
            to_flight_list.append(toFlight)

        # call to get flight details from destination to origin
        fromFlightDetails = str(
            itenerary_url + '/api/flight?origin=' + toAirport + '&destination=' + fromAirport + '&date=' + toDate)
        response = requests.request('GET', fromFlightDetails)
        fromFlightDetails = response.json()
        from_flight_list = []
        for f in fromFlightDetails:
            fromFlight = {
                "flight_id": f['id'],
                "price": f['price']['amount'],
                "origin_airport": f['legs'][0]['origin']['name'],
                "destination_airport": f['legs'][0]['destination']['name'],
                "departure": f['legs'][0]['departure'],
                "arrival": f['legs'][0]['arrival'],
                "duration": f['legs'][0]['duration'],
                "carrier": f['legs'][0]['carriers'][0]['name'],
            }
            from_flight_list.append(fromFlight)

        resp = {"org": fromLocation, "dest": toLocation, "dest_flights": to_flight_list[0],
                "return_flights": from_flight_list[0]}
        return resp
    else:
        resp = Response('NOT FOUND', status=404,
                       content_type='text/plain')
    return resp


# create user
@app.route("/users_service/signup", methods=["POST"])
def signup():
    if request.method == 'POST':
        fromLocation = request.get_json()['fromLocation']
        toLocation = request.get_json()['toLocation']
        fromDate = request.get_json()['fromDate']
        toDate = request.get_json()['toDate']

        # get src airport code
        getAirportCodeUrl = itenerary_url + '/api/flight/' \
                            + fromLocation
        response = requests.request('GET', getAirportCodeUrl)
        response = response.json()
        fromAirport = response[0]['code']

        # get dest airport code
        getAirportCodeUrl = itenerary_url + '/api/flight/' + toLocation
        response = requests.request('GET', getAirportCodeUrl)
        response = response.json()
        toAirport = response[0]['code']

        # call to get flight details from origin to destination
        toFlightDetails = str(
            itenerary_url + '/api/flight?origin=' + fromAirport + '&destination=' + toAirport + '&date=' + fromDate)
        response = requests.request('GET', toFlightDetails)
        toFlightDetails = response.json()
        to_flight_list = []
        for f in toFlightDetails:
            toFlight = {
                "flight_id": f['id'],
                "price": f['price']['amount'],
                "origin_airport": f['legs'][0]['origin']['name'],
                "destination_airport": f['legs'][0]['destination']['name'],
                "departure": f['legs'][0]['departure'],
                "arrival": f['legs'][0]['arrival'],
                "duration": f['legs'][0]['duration'],
                "carrier": f['legs'][0]['carriers'][0]['name'],
            }
            to_flight_list.append(toFlight)

        # call to get flight details from destination to origin
        fromFlightDetails = str(
            itenerary_url + '/api/flight?origin=' + toAirport + '&destination=' + fromAirport + '&date=' + toDate)
        response = requests.request('GET', fromFlightDetails)
        fromFlightDetails = response.json()
        from_flight_list = []
        for f in fromFlightDetails:
            fromFlight = {
                "flight_id": f['id'],
                "price": f['price']['amount'],
                "origin_airport": f['legs'][0]['origin']['name'],
                "destination_airport": f['legs'][0]['destination']['name'],
                "departure": f['legs'][0]['departure'],
                "arrival": f['legs'][0]['arrival'],
                "duration": f['legs'][0]['duration'],
                "carrier": f['legs'][0]['carriers'][0]['name'],
            }
            from_flight_list.append(fromFlight)

        resp = {"org": fromLocation, "dest": toLocation, "dest_flights": to_flight_list,
                "return_flights": from_flight_list}
        return resp
    else:
        resp = Response('NOT FOUND', status=404,
                       content_type='text/plain')
    return resp


# get userId by userName
@app.route("/users_service/get_user_id", methods=["POST"])
def getUserId():
    if request.method == 'POST':
        user_id_response = UserResource.get_user_id(request.get_json()['username'])

        if user_id_response:
            result = {'user_id': user_id_response}
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            result = {'success': False, 'message': 'user id could not be found'}
            rsp = Response(json.dumps(result), status=404, content_type="application.json")
    else:
        rsp = Response("Methods not defined", status=404, content_type="text/plain")
    return rsp


@app.route('/users_service/create_trip', methods=['POST'])
def create_new_trip():
    if request.method == 'POST':
        # trip_id is the itinerary_id sent from frontend
        print("printing_request", request.get_json())
        rsp = UserResource.create_new_trip(request.get_json()['user_id'], request.get_json()['trip_id'])
        # user_name = UserResource.get_user_name(request.get_json()['user_id'])
        # sns.publish(TopicArn='arn:aws:sns:us-east-2:641893269805:trip-notification', Message=str(user_name),
        #             Subject=str(request.get_json()['user_id']))
        # print('Notification Sent!')
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route('/users_service/delete_trip', methods=['POST'])
def delete_trip():
    if request.method == 'POST':
        # trip_id is the itinerary_id sent from frontend
        print("printing_request", request.get_json())
        result = UserResource.delete_trip(request.get_json()['trip_id'])
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route('/users_service/get_saved_trips', methods=['POST'])
def get_saved_trips():
    if request.method == 'POST':
        trips = UserResource.get_saved_trips(request.get_json()['user_id'])

        # iterate over trips and call itenerary service by each trip id
        saved_trips = []
        for t in trips:
            print("trip_id", t['trip_id'])
            req = str(itenerary_url + '/itenerary_service/get_trip?itenerary_id=' + str(t['trip_id']))
            response = requests.request('GET', req)
            saved_trips.append(response.json())

        # rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        saved_trips = Response("NOT FOUND", status=404, content_type="text/plain")
    return saved_trips


@app.route('/users_service/get_trips', methods=['GET'])
def get_trips():
    if request.method == 'GET':
        user = request.args.get("user_id")
        trips = UserResource.get_saved_trips(user)
        return trips
    else:
        trips = Response("NOT FOUND", status=404, content_type="text/plain")
    return trips

# old user login
@app.route("/users_service/login", methods=["POST"])
def login():
    if request.method == 'POST':
        user_id_response = UserResource.verify_login(request.get_json()['username'],
                                                     request.get_json()['password'])
        if user_id_response:
            result = {'success': True, 'message': 'login successful', 'user_id': user_id_response}
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            result = {'success': False, 'message': 'Wrong username or password'}
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("Methods not defined", status=404, content_type="text/plain")
    return rsp


# New login using google authentication
# The old sign up above needs to be removed
# For now initializing it as login version 2
@app.route("/users_service/login2", methods=["GET"])
def login2():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    print(authorization_endpoint)

    # Use library to construct the request for login and provide scopes that let you retrieve user's profile from Google
    request_url = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return {"request_url": request_url}

# user logout
@app.route("/users_service/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    # return {request_url: "http://localhost:3000/"}
    print("success here")
    return redirect("http://localhost:3000/")


@app.route("/users_service/login2/callback", methods=["GET", "POST"])
def callback():
    print("redirect123")
    # Get authorization code from Google sending back to user
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    print(f"token response: {token_response.json()}")
    print(f"code: {code}")
    # Parsing the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Find tokens and find the hitting URL
    # from Google that gives you user's information,
    # including their Google Profile Image and Email, but we can exclude the profile pic if is not implemented in UI
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    print(userinfo_endpoint)
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, and now we've verified their email through Google.
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        email = userinfo_response.json()["email"]
        username = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # no username
    print(unique_id)

    # Create a user in our db with the information provided
    # by Google
    user = User(id_=unique_id, email=email, name=username)
    # take to dashboard
    # Doesn't exist? Add to database
    # if user exist then display dashboard else display userinputs in the UI
    url = frontend_url+"loggedin/"+username 
    if not User.get(unique_id):
        User.create(unique_id, email, username)
        url = frontend_url+"userInputs/"+username
        # show form
    # Begin user session by logging the user in
    login_user(user)
    # return redirect(url_for("index"))
    return redirect(url)


@app.before_request
def check_valid_path():
    print("check")
    # enforce a google login
    print("check_valid_path")
    print(request.path)
    result_pass = security.check_path(request)
    print("result_pass: {}".format(result_pass))
    if not result_pass:
        print("request is blocked")
        # return redirect(url_for(login2))  # redirect to the frontend google auth page
        return "Invalid token", 401
    else:
        print("you are good to go")

@app.after_request
def after_request(response):
    # enforces sns message
    print("checking after request")
    if request.path == trigger_SNS_request["path"] and request.method == trigger_SNS_request["method"]:
        sns = notification.NotificationMiddlewareHandler.get_sns_client()
        print("Got SNS Client!")

        message = {"Test": "Notification sent"}
        notification.NotificationMiddlewareHandler.send_sns_message \
            ("arn:aws:sns:us-east-2:641893269805:trip-notification", message)
    return response

# # reset user password
# @app.route("/users_service/user/reset_password", methods=["POST"])
# def reset_password():
#     if request.method == 'POST':
#         user_id_res = UserResource.reset_password(request.get_json()['email'], request.get_json()['old_password'],
#                                                   request.get_json()['new_password'])
#         if user_id_res:
#             result = {'success': True, 'message': 'changing successful'}
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#         else:
#             result = {'success': False, 'message': 'Wrong username or password'}
#             rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("Methods not defined", status=404, content_type="text/plain")
#     return rsp


# # edit user profile
# This route does not make sense to have anymore
# @app.route("/users_service/user/edit/<user_id>", methods=["POST"])
# def edit_user(user_id):
#     if request.method == 'POST':
#         result = UserResource.edit_user(request.get_json()['user_first_name'],
#                                         request.get_json()['user_last_name'], user_id)
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("Methods not defined", status=404, content_type="text/plain")
#     return rsp


# get user
@app.route("/users_service/show_user/<user_id>", methods=["GET"])
def get_user(user_id):
    result = UserResource.get_user(user_id)
    print(result)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


# delete user
@app.route("/users_service/delete_user/<user_id>", methods=["GET"])
def delete_user(user_id):
    result = UserResource.delete_user(user_id)
    if result['success']:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response(json.dumps(result), status=404, content_type="application.json")
    return rsp


# # create trip
# @app.route('/users_service/create_new_trip/<user_id>', methods=['POST'])
# def create_new_trip(user_id):
#     if request.method == 'POST':
#         result = UserResource.create_new_trip(user_id, request.get_json()['destination'], request.get_json()['origin'],
#                                               request.get_json()['num_people'], request.get_json()['budget'])
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#     return rsp


# get trip
@app.route("/users_service/show_trips/<trip_id>", methods=["GET"])
def get_trip(trip_id):
    result = UserResource.get_trips(trip_id)
    print(result)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


# edit trip
@app.route("/users_service/edit_trips/<trip_id>", methods=["POST"])
def edit_trips(trip_id):
    if request.method == 'POST':
        result = UserResource.edit_trips(request.get_json()['destination'], request.get_json()['origin'],
                                         request.get_json()['num_people'], request.get_json()['budget'], trip_id)
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("Methods not defined", status=404, content_type="text/plain")
    return rsp



# # need to work on the integration test(?)
# # create new itinerary
# @app.route('/users_service/create_new_itinerary', methods=['POST'])
# def create_new_itinerary():
#     if request.method == 'POST':
#         result = UserResource.create_new_itinerary(request.get_json()['trip_id'], request.get_json()['total_cost'])
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#     return rsp
#
#
# # edit itinerary
# @app.route("/users_service/edit_itinerary/<itinerary_id>", methods=["POST"])
# def edit_itinerary(itinerary_id):
#     if request.method == 'POST':
#         result = UserResource.edit_itinerary(request.get_json()['total_cost'], itinerary_id)
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("Methods not defined", status=404, content_type="text/plain")
#     return rsp
#
#
# # delete itinerary
# @app.route("/users_service/delete_itinerary/<itinerary_id>", methods=["GET"])
# def delete_itinerary(itinerary_id):
#     result = UserResource.delete_itinerary(itinerary_id)
#     if result['success']:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response(json.dumps(result), status=404, content_type="application.json")
#     return rsp
#
#
# # get itinerary
# @app.route("/users_service/get_itinerary/<itinerary_id>", methods=["GET"])
# def get_itinerary(itinerary_id):
#     result = UserResource.get_itinerary(itinerary_id)
#     print(result)
#     if result:
#         rsp = Response(json.dumps(result), status=200, content_type="application.json")
#     else:
#         rsp = Response("NOT FOUND", status=404, content_type="text/plain")
#     return rsp


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5011)
