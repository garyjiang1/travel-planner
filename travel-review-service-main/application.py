from flask import Flask, Response, request
import json
from datetime import datetime
from review_resource import ReviewResource
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.get("/")
def get_service():
    msg = {
        "Service": "Review",
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


@application.route('/api/review', methods=['GET','DELETE','POST','PUT'])
def post_review():

    #handle the GET requests
    if request.method == 'GET':
        args = request.args
        limit, offset = None, None
        if 'limit' in args:
            limit = args.get("limit")
            if 'offset' in args:
                offset = args.get('offset')
        city = args.get('city')
        print(city)
        if ('user_id' in args) and ('city' in args):
            print('1')
            user_id = args.get('user_id')
            output = ReviewResource.get_review_by_city_and_user_id(city,user_id,limit,offset)
        elif 'user_id' in args:
            print('2')
            user_id = args.get('user_id')
            output = ReviewResource.get_review_by_user_id(user_id,limit,offset)
        else:
            print('3')
            output = ReviewResource.get_review_by_city(city,limit,offset)
        json_output = json.dumps(output)
        result = Response(json_output, status=200, content_type="application/json")
        return result

    # handle the DELETE request
    if request.method == 'DELETE':
        body = request.get_json()
        city = body['city']
        user_id = body['user_id']
        print(city)
        print(user_id)
        output = ReviewResource.delete_review(city,user_id)
        if (output==0):
            result = Response(json.dumps({"message": "resource not found", "status": 404}),status=404, content_type="application/json")
        else:
            result = Response(json.dumps({"message": "successfully deleted", "status": 200}), status=200, content_type="application/json")
        return result

    # handle the POST request
    if request.method == 'POST':
        body = request.get_json()
        city = body['city']
        user_id = body['user_id']
        review = body['review']
        rating = body['rating']
        ReviewResource.add_review(city,user_id,review,rating)
        result = Response(json.dumps(body), status=200, content_type="application/json")
        # result = Response(json.dumps(body), status=200, content_type="application/json",  headers={'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*', 'Access-Control-Allow-Origin':'*'})
        return result

    # handle the PUT request
    if request.method == 'PUT':
        body = request.get_json()
        city = body['city']
        user_id = body['user_id']

        #update the review and rating
        if ('review' in body) and ('rating' in body):
            review = body['review']
            rating = body['rating']
            ReviewResource.update_review_and_rating(city, user_id, review, rating)
        #update the rating
        elif('rating' in body):
            rating = body['rating']
            ReviewResource.update_rating(city, user_id, rating)
        #update the review
        else:
            review = body['review']
            ReviewResource.update_review(city,user_id,review)
        result = Response(json.dumps(body), status=200, content_type="application/json")
        return result


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host="0.0.0.0", port=5012)