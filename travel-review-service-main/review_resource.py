from typing import Optional

import pymysql

import os
import requests


class ReviewResource:

    def __int__(self):
        pass

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
    def get_review_by_city(city, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        sql = f'SELECT * FROM review_service.review where city like "%{city}%"';
        if additional != "":
            sql += additional
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        # res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_review_by_city_and_user_id(city, user_id, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        user = user_id
        sql = f'SELECT * FROM review_service.review where city like "%{city}%" and user_id={user}';
        if additional != "":
            sql += additional
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        # res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    def get_review_by_user_id(user_id, limit: Optional[int] = None, offset: Optional[int] = None):
        additional = ""
        if limit is not None:
            additional += f"&limit={limit}"
            if offset is not None:
                additional = f"&offset={offset}"
        user = user_id
        sql = f'SELECT * FROM review_service.review where user_id={user}';
        if additional != "":
            sql += additional
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        # res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    def add_review(city, user_id, review, rating):
        my_user = user_id
        sql = f'''INSERT INTO review_service.review(city, user_id, review, rating) VALUES ("{city}",{my_user},"{review}","{rating}")''';
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    def update_review(city, user_id, review):
        my_user = user_id
        sql = f'UPDATE review_service.review SET review="{review}" WHERE city="{city}" and user_id={my_user} ';
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    def update_rating(city, user_id, rating):
        my_user = user_id
        sql = f'UPDATE review_service.review SET rating={rating} WHERE city="{city}" and user_id={my_user} ';
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    def update_review_and_rating(city, user_id, review, rating):
        my_user = user_id
        sql = f'UPDATE review_service.review SET review="{review}", rating={rating} WHERE city="{city}" and user_id={my_user} ';
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        return res

    def delete_review(city, user_id):
        user = user_id
        sql = f'DELETE from review_service.review WHERE city="{city}" and user_id={user} ';
        print(sql)
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        print('---------------------')
        print(res)
        return res

    # get user id, not sure if this is needed, but you can invoke a call to user service.
    # (before making calls, make sure the environment variable in line 144 is set, and you need to have user_service running concurrently)
    # -Gary
    @staticmethod
    def _get_user_id(user_id):

        baseURL = os.environ.get("USER_SERVICE_URL")
        user_id = None
        res = requests.get(baseURL + f'/users_service/show_user/{user_id}').json()
        if res['success']:
            data = res['data'][1]
            user_id = list(data.values())[0]
        return user_id
