from flask_login import UserMixin
from user_service_resource import UserResource


class User(UserMixin):
    def __init__(self, id_, email, name):
        self.id = id_
        self.email = email
        self.name = name

    @staticmethod
    def get(user_id):
        user = UserResource.get_user(user_id)
        if not user:
            return None

        user = User(
            id_=user['user_id'], email=user['email'], name=user['username']
        )
        return user

    @staticmethod
    def create(id_, email, username):
        UserResource.google_login(id_, email, username)


if __name__ == "__main__":
    print(User.get('12345'))
