class UserProcessError(Exception):
    """
        Raise a user error
    """

    def _init_(self, message: str, status_code: int):
        Exception._init_(self, message)
        self.status_code = status_code
