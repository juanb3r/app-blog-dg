from .exceptions import (
    UserProcessError
)
from .models import (
    UserModel
)


class Queryset:

    @staticmethod
    def login_user(data: dict):
        try:
            user = UserModel.objects.get(
                email=data["email"],
                password=data["password"]
                )
        except UserModel.DoesNotExist:
            raise UserProcessError(
                "Invalited credential, wrong email or passsword",
                400
            )
        return {
            "message": "Login successfully",
            "data": {
                "user_rol": user.id_rol.name_rol,
                "id_user": user.id_user
            }
        }
