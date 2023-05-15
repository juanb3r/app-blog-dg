from .exceptions import UserProcessError
from .helpers import (
    check_create_permission,
    check_update_permission,
    hash_sha256,
    user_login_process,
    user_logout_process,
)
from .models import (
    CommentsModel,
    EntryModel,
    LikesModel,
    ProfileModel,
    RolModel,
    UserModel,
)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id_user',
            'id_rol',
            'fullname',
            'password',
            'email',
            'created_at',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `UserModel` instance, given the validated data.
        """
        validated_data['password'] = hash_sha256(
            validated_data.get('password')
        )
        return UserModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserModel` instance, given the validated data.
        """
        if check_update_permission():
            instance.id_user = validated_data.get('id_user', instance.id_user)
            instance.id_rol = validated_data.get('id_rol', instance.id_rol)
            instance.fullname = validated_data.get(
                'fullname',
                instance.fullname
            )
            instance.password = hash_sha256(
                validated_data.get('password', instance.password)
            )
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolModel
        fields = [
            'id_rol',
            'name_rol',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `RolModel` instance, given the validated data.
        """
        return RolModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `RolModel` instance, given the validated data.
        """
        instance.name_rol = validated_data.get('name_rol', instance.name_rol)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = [
            'id_profile',
            'id_user',
            'biography',
            'image',
            'created_at',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `ProfileModel` instance, given the validated data.
        """
        if check_create_permission():
            return ProfileModel.objects.create(**validated_data)
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )

    def update(self, instance, validated_data):
        """
        Update and return an existing `ProfileModel` instance, given the validated data.
        """
        if check_update_permission():
            instance.id_user = validated_data.get('id_user', instance.id_user)
            instance.biography = validated_data.get(
                'biography',
                instance.biography
            )
            instance.image = validated_data.get('image', instance.image)
            instance.save()
            return instance
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryModel
        fields = [
            'id_entry',
            'id_user',
            'titles',
            'content',
            'category',
            'tags',
            'created_at',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `EntryModel` instance, given the validated data.
        """
        if check_create_permission():
            return EntryModel.objects.create(**validated_data)
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )

    def update(self, instance, validated_data):
        """
        Update and return an existing `EntryModel` instance, given the validated data
        """
        if check_update_permission():
            instance.id_user = validated_data.get('id_user', instance.id_user)
            instance.titles = validated_data.get('titles', instance.titles)
            instance.content = validated_data.get('content', instance.content)
            instance.category = validated_data.get(
                'category',
                instance.category
            )
            instance.tags = validated_data.get('tags', instance.tags)
            instance.save()
            return instance
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesModel
        fields = [
            'id_like',
            'id_user',
            'id_entry',
            'id_comment',
            'created_at',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `LikesModel` instance, given the validated data.
        """
        if check_create_permission():
            if (
                validated_data.get('id_entry') or
                validated_data.get('id_comment')
            ):
                return LikesModel.objects.create(**validated_data)
            raise UserProcessError(
                "In the data are missing id_comment or id_entry",
                400
            )
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )

    def update(self, instance, validated_data):
        """
        Update and return an existing `LikesModel` instance, given the validated data.
        """
        if check_update_permission():
            instance.id_user = validated_data.get('id_user', instance.id_user)
            instance.id_entry = validated_data.get(
                'id_entry',
                instance.id_entry
            )
            instance.id_comment = validated_data.get(
                'id_comment',
                instance.id_comment
            )
            instance.save()
            return instance
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = [
            'id_comment',
            'id_user',
            'id_entry',
            'comment',
            'created_at',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `CommentsModel` instance, given the validated data.
        """
        if check_create_permission():
            return CommentsModel.objects.create(**validated_data)
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )

    def update(self, instance, validated_data):
        """
        Update and return an existing `CommentsModel` instance, given the validated data.
        """
        if check_update_permission(instance.id_user):
            instance.id_user = validated_data.get('id_user', instance.id_user)
            instance.id_entry = validated_data.get(
                'id_entry',
                instance.id_entry
            )
            instance.comment = validated_data.get('comment', instance.comment)
            instance.save()
            return instance
        raise UserProcessError(
            "It is unauthorized, refusing  requested resource",
            403
        )


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'password',
            'email',
        ]
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        """
        Create and return a new `LoginModel` instance, given the validated data.
        """
        login = user_login_process(
            {
                'email': validated_data["email"],
                'password': validated_data["password"]
            }
        )
        validated_data.update(login)
        return validated_data


class UserLogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = []
        read_only_fields = ()

    def create(self, validated_data):
        """
        Create and return a new `LogoutModel` instance, given the validated data.
        """
        logout = user_logout_process()
        validated_data.update(logout)
        return validated_data
