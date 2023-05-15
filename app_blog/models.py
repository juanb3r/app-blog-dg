from django.db import models


class UserModel(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    id_rol = models.ForeignKey(
        'RolModel',
        on_delete=models.CASCADE,
    )
    fullname = models.CharField(max_length=40)
    password = models.TextField()
    email = models.EmailField(
        max_length=40
    )
    created_at = models.DateTimeField(auto_now_add=True)


class ProfileModel(models.Model):
    id_profile = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(
        'UserModel',
        unique=True,
        on_delete=models.CASCADE,
    )
    biography = models.TextField()
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class RolModel(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    name_rol = models.CharField(
        unique=True,
        max_length=40
    )


class EntryModel(models.Model):
    id_entry = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(
        'UserModel',
        on_delete=models.CASCADE,
    )
    titles = models.CharField(max_length=40)
    content = models.CharField(max_length=100)
    category = models.CharField(max_length=40)
    # todo guardar una lista
    tags = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentsModel(models.Model):
    id_comment = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(
        'UserModel',
        on_delete=models.CASCADE,
    )
    id_entry = models.ForeignKey(
        'EntryModel',
        on_delete=models.CASCADE,
    )
    comment = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)


class LikesModel(models.Model):
    id_like = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(
        'UserModel',
        on_delete=models.CASCADE,
    )
    id_entry = models.ForeignKey(
        'EntryModel',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    id_comment = models.ForeignKey(
        'CommentsModel',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
