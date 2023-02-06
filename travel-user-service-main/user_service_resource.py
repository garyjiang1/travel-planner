from datetime import datetime
import os
from typing import Optional

import pymysql

class UserResource:

    def __int__(self):
        self.current_time = datetime.now

    @staticmethod
    def _get_connection():
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
    def signup(email, username, password, ):
        sql = "INSERT INTO user_service.user (email, username, password) " \
              "VALUES (%s, %s, %s);"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            res = cur.execute(sql, args=(email, username, password))
            result = {'success': True, 'message': 'Register successfully, continue to log in'}
        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': 'This email is already registered, try another one'}
        return result

    # New user login
    # Removed password because the authentication is done through Google
    @staticmethod
    def google_login(id, email, username):
        sql = "SELECT * FROM user_service.user where email=%s"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        # if the user does not exist, insert into user table
        cur.execute(sql, args=email)
        res = cur.fetchone()
        if not res:
            print('Insert new user')
            sql_i = "INSERT INTO user_service.user (user_id, email, username) VALUES (%s, %s, %s);"
            cur.execute(sql_i, args=(id, email, username))
            sql = "SELECT * FROM user_service.user where email=%s"
            cur.execute(sql, args='email')
            res = cur.fetchone()
        return res

    @staticmethod
    def create_new_trip(user_id, trip_id):
        sql = "INSERT INTO user_service.trips(user_id, trip_id) VALUES( %s, %s);"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args=(user_id, trip_id))
            result = {'success': True, 'message': 'Added new trip'}
        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': 'Something wrong with adding new trip...'}
        return result

    @staticmethod
    def delete_trip(trip_id):
        sql = "DELETE FROM user_service.trips WHERE trip_id=%s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args=(trip_id))
            result = {'success': True, 'message': 'Delete trip'}
        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': 'Something wrong with deleting trip...'}
        return result

    @staticmethod
    def get_saved_trips(user_id):
        sql = "SELECT trip_id FROM user_service.trips WHERE user_id=%s"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=user_id)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_user_name(user_id):
        sql = "SELECT username FROM user_service.user WHERE user_id=%s"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=user_id)
        result = cur.fetchone()

        return result































    @staticmethod
    def verify_login(username, password):
        sql = "SELECT user_id FROM user_service.user WHERE username=%s AND password=%s"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(username, password))
        result = cur.fetchone()
        user_id = result['user_id'] if result else None

        return user_id

    # @staticmethod
    # def edit_user(user_first_name, user_last_name, user_id):
    #     sql_p = "SELECT * FROM user_service.user WHERE user_id = %s;"
    #     sql = "UPDATE user_service.user \
    #                SET user_first_name=%s, user_last_name=%s \
    #                WHERE user_id=%s;"
    #     conn = UserResource._get_connection()
    #     cur = conn.cursor()
    #     try:
    #         cur.execute(sql_p, args=user_id)
    #         res = cur.fetchone()
    #         if res:
    #             cur.execute(sql, args=(user_first_name, user_last_name, email, user_id))
    #             result = {'success': True, 'message': 'You have successfully edited the profile'}
    #         else:
    #             result = {'success': False, 'message': 'You fail to edit the profile'}
    #
    #     except pymysql.Error as e:
    #         print(e)
    #         result = {'success': False, 'message': str(e)}
    #     return result

    @staticmethod
    def reset_password(email, old_password, new_password):
        sql_p = "SELECT user_id FROM user_service.user WHERE email=%s and password=%s;"
        sql = "UPDATE user_service.user \
                       SET password=%s \
                       WHERE email=%s AND password= %s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_p, args=(email, old_password))
            res = cur.fetchone()
            if res:
                cur.execute(sql, args=(new_password, email, old_password))
                result = {'success': True, 'message': 'Resetting successfully, continue to log in'}
            else:
                result = {'success': False, 'message': 'Forget your password?'}

        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': 'Anything wrong with password...'}
        return result

    @staticmethod
    def get_user(user_id):
        sql = "SELECT * FROM user_service.user WHERE user_id=%s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=user_id)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_user_id(username):
        sql = "SELECT user_id FROM user_service.user WHERE username=%s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=username)
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_user(user_id):
        sql_p = "SELECT * FROM user_service.user WHERE user_id=%s;"
        sql = "DELETE FROM user_service.user WHERE user_id = %s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_p, args=user_id)
            res = cur.fetchone()
            if res:
                cur.execute(sql, args=user_id)
                result = {'success': True, 'message': 'You have deleted the user'}
            else:
                result = {'success': False, 'message': 'Something wrong with deleting user'}

        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': str(e)}
        return result

    @staticmethod
    def get_trips(trip_id, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        sql = "SELECT * FROM user_service.trips WHERE trip_id=%s"
        if additional != "":
            sql += additional
        conn = UserResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=trip_id)
        result = cur.fetchone()

        return result

    @staticmethod
    def edit_trips(destination, origin, num_people, budget, trip_id):
        sql_p = "SELECT * FROM user_service.trips WHERE trip_id=%s;"
        sql = "UPDATE user_service.trips \
                       SET destination=%s, origin=%s,  num_people=%s , budget=%s\
                       WHERE trip_id=%s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_p, args=trip_id)
            res = cur.fetchone()
            if res:
                cur.execute(sql, args=(destination, origin, num_people, budget, trip_id))
                result = {'success': True, 'message': 'Updated trip successfully'}
            else:
                result = {'success': False, 'message': 'Something wrong with updating trip'}

        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': str(e)}
        return result

    @staticmethod
    def delete_trip(trip_id):
        sql_p = "SELECT * FROM user_service.trips WHERE trip_id=%s;"
        sql = "DELETE FROM user_service.trips WHERE trip_id = %s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_p, args=trip_id)
            res = cur.fetchone()
            if res:
                cur.execute(sql, args=trip_id)
                result = {'success': True, 'message': 'You have deleted the trip'}
            else:
                result = {'success': False, 'message': 'Something wrong with deleting trip'}

        except pymysql.Error as e:
            print(e)
            res = 'ERROR'
            result = {'success': False, 'message': str(e)}
        return result

    @staticmethod
    def create_new_itinerary(trip_id, total_cost):
        sql = "INSERT INTO user_service.itinerary(trip_id, total_cost) VALUES( %s, %s);"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql, args=(trip_id, total_cost))
            result = {'success': True, 'message': 'New itinerary registered successfully'}
        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': 'Something wrong with creating itinerary'}
        return result

    @staticmethod
    def edit_itinerary(total_cost, itinerary_id):
        sql_p = "SELECT * FROM user_service.itinerary WHERE itinerary_id=%s;"
        sql = "UPDATE user_service.itinerary SET total_cost=%s WHERE itinerary_id=%s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_p, args=itinerary_id)
            res = cur.fetchone()
            if res:
                cur.execute(sql, args=(total_cost, itinerary_id))
                result = {'success': True, 'message': 'Updated itinerary successfully'}
            else:
                result = {'success': False, 'message': 'Something wrong with updating itinerary'}
        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': 'ERROR'}
        return result

    @staticmethod
    def delete_itinerary(itinerary_id):
        sql_p = "SELECT * FROM user_service.itinerary WHERE itinerary_id=%s;"
        sql = "DELETE FROM user_service.itinerary WHERE itinerary_id = %s;"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql_p, args=itinerary_id)
            res = cur.fetchone()
            if res:
                cur.execute(sql, args=itinerary_id)
                result = {'success': True, 'message': 'You have deleted the itinerary'}
            else:
                result = {'success': False, 'message': 'Something wrong with deleting itinerary'}

        except pymysql.Error as e:
            print(e)
            result = {'success': False, 'message': str(e)}
        return result

    @staticmethod
    def get_itinerary(key):
        sql = "SELECT * FROM user_service.itinerary WHERE itinerary_id=%s"
        conn = UserResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        if result:
            result = {'success': True, 'data': res}
        else:
            result = {'success': False, 'message': 'Not Found', 'data': res}

        return result
