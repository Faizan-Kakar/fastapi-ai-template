import jwt, datetime
from app.core.config import SECRET_KEY


def create_jwt(email: str):
    payload = {
        "sub": email,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


ALGORITHM = "HS256"


def decode_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except Exception as e:
        return e