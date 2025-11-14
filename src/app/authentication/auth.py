# User authentication  -- bascailly to protect my apis only authenticated users can use that
# oauth2_scheme is depneddency procided by fastapi
# exrract the token fron teh authorization headwer

# have  2 methods to create an access token and validate an access token

# we will create access tokens
# we will be using jwt authentication

from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from authlib.jose import JoseError, jwt

# create some constants
SECRET_KEY = 'MY_SECRET'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRATION_MINUTES = 30


# CREATE ACCESS TOKENS
def create_access_tokens(data: dict) -> str:
    header = {'alg': ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(
        ACCESS_TOKEN_EXPIRATION_MINUTES)  # token will be availble from current time +30 mins
    payload = data.copy()  # copy is a featcure of dictionary or map object
    payload.update({'exp': expire})  # we can update the map
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')


# validatidn or decoding the token
def validate_token(token: str) -> str:
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        username = claims.get('sub')
        if username is None:
            raise HTTPException(status_code=410, detail="Token is incorrect")
        else:
            return username
    except JoseError:
        raise HTTPException(status_code=401, detail="Unable to validate the token")
