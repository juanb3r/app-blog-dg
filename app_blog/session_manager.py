class SessionManager:
    def __init__(self) -> None:
        self.__user_rol: str = ''
        self.__id_user: int = 0
        self.__is_logged: bool = False

    def get_login_status(self) -> bool:
        return self.__is_logged

    def get_user_rol(self) -> str:
        return self.__user_rol

    def get_id_user(self) -> int:
        return self.__id_user

    def login(self, user_rol: str, id_user: int):
        self.__user_rol = user_rol
        self.__id_user = id_user
        self.__is_logged = True

    def logout(self):
        self.__is_logged = False
        self.__user_rol = ''
        self.__id_user = 0
