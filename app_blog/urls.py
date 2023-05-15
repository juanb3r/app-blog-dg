from rest_framework import routers
from .views import (
    CommentsViewSet,
    EntryViewSet,
    LikesViewSet,
    LoginViewSet,
    ProfileViewSet,
    RolViewSet,
    UserViewSet,
    LogoutViewSet,
)


router = routers.DefaultRouter()

router.register('api/login', LoginViewSet, 'login')
router.register('api/logout', LogoutViewSet, 'logout')
router.register('api/user', UserViewSet, 'user')
router.register('api/rol', RolViewSet, 'rol')
router.register('api/profile', ProfileViewSet, 'profile')
router.register('api/entry', EntryViewSet, 'entry')
router.register('api/likes', LikesViewSet, 'likes')
router.register('api/comments', CommentsViewSet, 'comments')

urlpatterns = router.urls
