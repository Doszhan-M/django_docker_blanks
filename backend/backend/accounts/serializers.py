from rest_framework_simplejwt.tokens import RefreshToken
from djoser.serializers import UserCreateSerializer, UserSerializer


class RegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'email', 'phone', 'password', )

    def to_representation(self, instance):
        data = super(RegistrationSerializer, self).to_representation(instance)
        user_tokens = RefreshToken.for_user(instance)
        tokens = {'refresh': str(user_tokens), 'access': str(user_tokens.access_token)}
        data.update(tokens)
        return data


class UserMeSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('username', 'email', 'phone', )