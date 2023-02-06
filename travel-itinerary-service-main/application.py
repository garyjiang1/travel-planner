from flask import Flask, Response, request
import json
from datetime import datetime
from pprint import pprint
import requests
import time
from travel_resource import TravelResource
from flask_cors import CORS


FLIGHT_URL = "https://skyscanner50.p.rapidapi.com/api/v1/searchFlights"
AIRPORT_URL = "https://skyscanner50.p.rapidapi.com/api/v1/searchAirport"
HEADERS = {
	"X-RapidAPI-Key": "93737493e5mshd05edb373f53a7fp1c9674jsn6a8356e0c98d",
	"X-RapidAPI-Host": "skyscanner50.p.rapidapi.com"
}
application = Flask(__name__)

CORS(application)


@application.get("/")
def get_service():
    msg = {
        "Service": "Itenerary Service",
        "Description": "Service to manage reviews for cities"
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@application.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "Flask Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@application.route('/api/flight', methods=['GET'])
def get_flight():

    if request.method == 'GET':
        args = request.args
        origin = args.get('origin')
        destination = args.get('destination')
        date = args.get('date')

        # origin_code = get_airpoirt_code(origin)
        # destination_code = get_airpoirt_code(destination)

        querystring = {"origin": origin, "destination": destination, "date": date}
        response = requests.request("GET", FLIGHT_URL, headers=HEADERS, params=querystring)
        # print("response"+response)

        time.sleep(3)
        response = response.json()
        print("this is the response", response)
        if response['status'] == False:
            return Response({"error": response['message']}, status=500, content_type="application/json")
        data = response['data']

        flight_data = sorted(data, key=lambda x: x["price"]["amount"])
        # pprint(flight_data)

        flights = []
        for i in range(0,5):
            flights.append(flight_data[i])
            pprint(flight_data[i])

        result = Response(json.dumps(flights), status=200, content_type="application/json")
        return result


@application.route('/itenerary_service/get_trip', methods=['GET'])
def get_trips_by_itenerary_id():
    if request.method == 'GET':
        args = request.args
        itenerary_id = args.get('itenerary_id')
        itenerary_resp = TravelResource.get_trips_by_itenerary_id(itenerary_id)
    else:
        itenerary_resp = Response("NOT FOUND", status=404, content_type="text/plain")
    return itenerary_resp

@application.route('/api/flight/<location>', methods=['GET'])
def get_airpoirt_code(location):
    querystring = {"query": location}
    response = requests.request("GET", AIRPORT_URL, headers=HEADERS, params=querystring)
    time.sleep(1)
    airport_data = response.json()
    data = airport_data['data']
    airports = []
    for airport in data:
        if 'PlaceId' in airport:
            airport_info = {"name": airport['PlaceName'], "code": airport['PlaceId']}
        else:
            continue
        #     airport_info = {"name": airport['PlaceName'], "code": airport['PlaceId']}
        airports.append(airport_info)
    result = Response(json.dumps(airports), status=200, content_type="application/json")
    return result

@application.route('/api/flight/update', methods=['GET','DELETE','POST','PUT'])
def update_flight():
    #handle the GET requests
    if request.method == 'GET':
        args = request.args
        limit, offset = None, None
        if 'limit' in args:
            limit = args.get("limit")
            if 'offset' in args:
                offset = args.get('offset')
        if ('origin' in args) and ('destination' in args):
            print('1')
            origin = args.get('origin')
            destination = args.get('destination')
            output = TravelResource.get_travel_by_origin_and_destination(origin, destination, limit, offset)
        elif ('origin_code' in args) and ('destination_code' in args):
            print('2')
            origin_code = args.get('origin_code')
            destination_code = args.get('destination_code')
            output = TravelResource.get_travel_by_code(origin_code, destination_code, limit, offset)
        elif 'itinerary_id' in args:
            print('3')
            itinerary_id = args.get('itinerary_id')
            output = TravelResource.get_travel_by_itinerary_id(itinerary_id, limit, offset)
        else:
            return Response("NOT FOUND!", status=404, content_type="application/json")

        result = Response(json.dumps(output, default=str), status=200, content_type="application/json")
        return result

    # handle the DELETE request
    if request.method == 'DELETE':
        body = request.get_json()
        travel_id = body['travel_id']
        print(travel_id)
        output = TravelResource.delete_travel(travel_id)
        if (output == 0):
            result = Response(json.dumps({"message": "resource not found", "status": 404}),status=404, content_type="application/json")
        else:
            result = Response(json.dumps({"message": "successfully deleted", "status": 200}), status=200, content_type="application/json")
        return result

    # handle the POST request
    if request.method == 'POST':
        body = request.get_json()
        itinerary_id = body['itinerary_id']
        review_id = body['review_id']
        origin = body['origin']
        destination = body['destination']
        origin_code = body['origin_code']
        destination_code = body['destination_code']
        departure_time = body['departure_time']
        arrival_time = body['arrival_time']
        airline_name = body['airline_name']
        flight_num  = body['flight_num']
        cost = float(body['cost'])
        # ori_airport, dst_airport, flight_num, airline_name, cost, dep_time, arr_time

        TravelResource.add_travel(itinerary_id, review_id, origin, destination, origin_code, \
            destination_code, departure_time, arrival_time, airline_name, flight_num, cost)
        result = Response(json.dumps(body), status=200, content_type="application/json")

        return result

    # handle the PUT request
    if request.method == 'PUT':
        body = request.get_json()
        travel_id = body['travel_id']

        #update the origin and destination
        if ('origin' in body) and ('destination' in body) and ('origin_code' in body) and ('destination_code' in body):
            origin = body['origin']
            destination = body['destination']
            origin_code = body['origin_code']
            destination_code = body['destination_code']
            TravelResource.update_origin_and_destination(origin, destination, origin_code, destination_code, travel_id)
        else:
            return Response("NOTHING TO UPDATE", status=404, content_type="application/json")
        result = Response(json.dumps(body), status=200, content_type="application/json")
        return result

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host="0.0.0.0", port=5000)