from typing import AnyStr
import bcrypt

PASSWORD_BCRYPT = 1
PASSWORD_DEFAULT = PASSWORD_BCRYPT

PASSWORD_BCRYPT_DEFAULT_COST = 10


def password_hash(password: AnyStr, algorithm=PASSWORD_DEFAULT) -> str:
    if isinstance(password, str):
        password = password.encode()
    salt = bcrypt.gensalt(PASSWORD_BCRYPT_DEFAULT_COST, prefix=b'2a')
    return bcrypt.hashpw(password, salt=salt).decode()


def password_verify(password: AnyStr, hashed_password: AnyStr) -> bool:
    if isinstance(password, str):
        password = password.encode()
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode()
    return bcrypt.checkpw(password, hashed_password)
