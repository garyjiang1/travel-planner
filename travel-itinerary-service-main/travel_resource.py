from datetime import date, datetime, timedelta
from typing import Optional

import pymysql

import os

class TravelResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        print("_get_connection")
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn

    @staticmethod
    def get_travel_by_origin_and_destination(origin, destination, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        sql = f'SELECT * FROM travel_service.Travel where origin like "%{origin}%" and destination like "%{destination}%"'
        if additional != "":
            sql += additional
        print(sql)
        conn = TravelResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        # res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_travel_by_code(origin_code, destination_code, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        sql = f'SELECT * FROM travel_service.Travel where origin_code like "%{origin_code}%" and destination_code like "%{destination_code}%"'
        if additional != "":
            sql += additional
        print(sql)
        conn = TravelResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        # res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_travel_by_itinerary_id(itinerary_id, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        itinerary = int(itinerary_id)
        sql = f'SELECT * FROM travel_service.Travel where itinerary_id = {itinerary}'
        if additional != "":
            sql += additional
        print(sql)
        conn = TravelResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        # res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def add_travel(itinerary_id, review_id, origin, destination, origin_code, \
            destination_code, departure_time, arrival_time, airline_name, flight_num, cost):
        itinerary = int(itinerary_id)
        review = int(review_id)
        sql = f'''INSERT INTO travel_service.Travel(itinerary_id, review_id, origin, destination, origin_code, destination_code, departure_time, arrival_time, airline_name, flight_num, cost) VALUES ({itinerary},{review},"{origin}","{destination}","{origin_code}","{destination_code}","{departure_time}","{arrival_time}","{airline_name}","{flight_num}",{cost})'''
        print(sql)
        conn = TravelResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res
        
    @staticmethod
    def get_trips_by_itenerary_id(itinerary_id):
        sql = f"SELECT * FROM travel_service.Travel WHERE itinerary_id=%s";
        print(sql)
        conn = TravelResource._get_connection()
        print(conn)
        cur = conn.cursor()
        res = cur.execute(sql, args=itinerary_id)
        result = cur.fetchone()
        print(result)
        return result

    @staticmethod
    def update_origin_and_destination(origin, destination, origin_code, destination_code, travel_id):
        travel = int(travel_id)
        sql = f'UPDATE travel_service.Travel SET origin="{origin}", destination="{destination}", origin_code="{origin_code}", destination_code="{destination_code}" WHERE travel_id="{travel}" '
        print(sql)
        conn = TravelResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    @staticmethod
    def delete_travel(travel_id):
        travel = int(travel_id)
        sql = f'DELETE from travel_service.Travel WHERE travel_id={travel} '
        print(sql)
        conn = TravelResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        print('---------------------')
        print(res)
        return res

