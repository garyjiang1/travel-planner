class ReviewCruds:

    def __int__(self):
        pass

    def sql_insert_review(review_id, city, rating, user_id, review):
        return f'INSERT INTO reviews (review_id, city, rating, user_id, review) VALUES({review_id}, {city}, {rating}, {user_id}, {review})'

    def sql_select_review_by_review_id(review_id):
        return f"SELECT * FROM reviews WHERE review_id={review_id}"

    def sql_update_review(review_id, rating, review):
        return f"UPDATE reviews SET rating={rating}, review={review} WHERE review_id={review_id}"

    def sql_delete_review_by_id(review_id):
        return f"DELETE FROM reviews WHERE review_id={review_id}"