# this is utility file which checks
# library for password hashing
from passlib.context import CryptContext

# Initialize password context
password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    Bcrypt has a 72-byte limit, so we truncate if necessary.
    """
    # Convert to bytes and truncate to 72 bytes if needed
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return password_context.hash(password_bytes.decode('utf-8'))


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hash.
    """
    password_bytes = plain_password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return password_context.verify(password_bytes.decode('utf-8'), hashed_password)


# Pre-compute hash once (not on every import)
# Generate this once and store it statically
_hashed_password = hash_password('secret123')

# we will simulate a db
fake_db = {
    "rohit": {
        'username': 'rohit',
        'hashed_password': _hashed_password
    }
}


# check and return user data
def get_user_from_db(username: str) -> dict | None:
    return fake_db.get(username)


if __name__ == '__main__':
    user_details = get_user_from_db("rohit")
    if user_details:
        print(user_details.get("username"))
    else:
        print("User not found")

    # Test password verification
    test_password = "secret123"
    stored_hash = fake_db["rohit"]["hashed_password"]
    print(f"Password verification: {verify_password(test_password, stored_hash)}")