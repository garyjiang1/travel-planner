import os
from user_service_resource import UserResource
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer

SECRET_KEY = os.urandom(24)
serializer = Serializer(SECRET_KEY)

# paths that do not require login
BLACKLISTED_PATHS = ['/users_service/get_trips']


def generate_auth_token(payload: dict) -> str:
    token = Serializer.dumps(payload)
    return token.decode('ascii')


def verify_auth_token(token: str) -> dict:
    try:
        data = Serializer.loads(token.encode('ascii'))
        # ['user_id']
        return data
    except (SignatureExpired, BadSignature) as e:
        return None


def check_path(request):
    # if request.path not in WHITELISTED_PATH:  # no need for checking google-auth status
    #     return True
    # else:
    # check if the user is logged in
    print(request.path)
    if request.path not in BLACKLISTED_PATHS:  # no need for checking google-auth status
        return True
    else:
        # check if the user is logged in
        user_id = request.args.get("user_id")
        print("here is user id {user_id}")
        user = UserResource.get_user(user_id)
        # double-checking if the user is in db
        if user:
            print("'user_id': {}".format(user))
            return True
        else:
            print("'user_id': {} not exists".format(user))
            return False
