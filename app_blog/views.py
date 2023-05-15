from .models import (
    CommentsModel,
    EntryModel,
    LikesModel,
    ProfileModel,
    RolModel,
    UserModel,
)
from .serializers import (
    CommentsSerializer,
    EntrySerializer,
    LikesSerializer,
    ProfileSerializer,
    RolSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
    UserSerializer,
)
from rest_framework import (
    mixins,
    permissions,
    viewsets,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = RolModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RolSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = EntryModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EntrySerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = LikesModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LikesSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = CommentsModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentsSerializer


class LoginViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer


class LogoutViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLogoutSerializer
