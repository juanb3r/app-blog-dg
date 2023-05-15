import hashlib
from .exceptions import UserProcessError
from .querysets import Queryset
from .session_manager import SessionManager


session_manager = SessionManager()


def hash_sha256(password: str) -> str:
    """
    Hashcheamos la contraseña con sha256

    Args:
        password (str): clave plana

    Returns:
        str: clave en sha256
    """
    hashed_password = hashlib.sha256(password.encode())
    password = hashed_password.hexdigest()
    return password


def user_login_process(data: dict):
    if not session_manager.get_login_status():
        data["password"] = hash_sha256(data["password"])
        response = Queryset.login_user(data)
        if response.get("data").get("user_rol"):
            session_manager.login(
                response.get("data").get("user_rol"),
                response.get("data").get("id_user")
            )
            return response
        raise UserProcessError(
            "This user doesn't exist",
            404
        )
    raise UserProcessError(
        "The user is already logged",
        409
    )


def user_logout_process():
    if session_manager.get_login_status():
        session_manager.logout()
        return {
            "message": "Logout successfully"
        }
    raise UserProcessError(
        "The user is not login",
        409
    )


def check_create_permission() -> bool:
    if (
            session_manager.get_login_status() and
            session_manager.get_user_rol() == "administrador" or
            session_manager.get_user_rol() == "editor" or
            session_manager.get_user_rol() == "blogger"
    ):
        return True
    return False


def check_update_permission(id_user: int) -> bool:
    if (
            session_manager.get_login_status() and
            session_manager.get_user_rol() == "administrador" or
            session_manager.get_user_rol() == "editor"
    ):
        return True
    elif (
            session_manager.get_login_status() and
            session_manager.get_user_rol() == "blogger" and
            session_manager.get_id_user() == id_user
    ):
        return True
    return False


def get_id_user() -> int:
    return session_manager.get_id_user()
