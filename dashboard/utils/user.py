import re
from typing import Tuple

MAX_USERNAME_LENGTH = 30
MIN_USERNAME_LENGTH = 2

MAX_FIRSTNAME_LENGTH = 30
MIN_FIRSTNAME_LENGTH = 1

MAX_PASSWORD_LENGTH = 30
MIN_PASSWORD_LENGTH = 2

PASSWORD_ALLOWED_CHARS = "A-Za-z0-9@#$%^&+="
PASSWORD_REQUIREMENTS = (
    f"""Your password must consist of these characters: {PASSWORD_ALLOWED_CHARS}
Your password must be at least {MIN_PASSWORD_LENGTH} characters long"""
)


def check_if_user_exists(
        username: str, password: str
) -> bool:
    """
    Check whether the user with the given username and password exists
    :param username:
    :param password:
    :return: True if the user exists otherwise False
    """
    # TODO: implement it
    raise NotImplementedError()


def create_new_user(
        username: str,
        password: str,
        firstname: str,
        gender: str
):
    # TODO: implement it
    raise NotImplementedError()


def check_password(password: str) -> Tuple[bool, str]:
    """
    Checks the password for the minimum requirements
    :param password: string from user
    :return:
        flag: True if the password is valid
        message: password requirements if it is not valid
    """

    if len(password) < MIN_PASSWORD_LENGTH:
        return (
            False,
            f"Your password must be at least {MIN_PASSWORD_LENGTH} "
            f"characters long"
        )

    if not re.match(rf"^[{PASSWORD_ALLOWED_CHARS}]+$", password):
        return False, PASSWORD_REQUIREMENTS

    return True, ""


def check_username(username: str) -> Tuple[bool, str]:
    """
    Checks if the given username already exists or it uses incorrect characters
    :param username: string from user
    :return:
        flag: True if the username does not exist and it is correct
        message: what the user must change in the written username
    """

    # TODO: check if the given username already exists
    if len(username) < MIN_USERNAME_LENGTH:
        return (
            False,
            f"Your username must be at least {MIN_USERNAME_LENGTH} "
            f"characters long"
        )
    return True, ""


def check_firstname(firstname: str) -> Tuple[bool, str]:
    """
    Checks if the given firstname uses incorrect characters
    :param firstname: string from user
    :return:
        flag: True if the username is correct
        message: what the user must change in the written firstname
    """
    if len(firstname) < MIN_FIRSTNAME_LENGTH:
        return (
            False,
            f"Your first name must be at least {MIN_FIRSTNAME_LENGTH} "
            f"characters long"
        )
    return True, ""
