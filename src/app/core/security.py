from datetime import timedelta, datetime, timezone
from app.core.config import settings


# create atoken
def create_token(data: dict, expire_minutes=30) -> str:
    to_encode = data.copy()  # take a copy of the original data
    expire_time = datetime.now(timezone.utc) + timedelta(expire_minutes)
    to_encode.update({'exp': expire_time})
    print(f'jwt Algo is  key is {settings.JWT_ALGORITHM}')
    return "encoded string"  # replace with real implemenation


def verify_token():
    try:
        print(f'settings url is {settings.REDIS_URL}')

    except Exception as e:
        print(e)
