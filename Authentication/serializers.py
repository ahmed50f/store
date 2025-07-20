from rest_framework import serializers
from .models import User as AuthenticationUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticationUser
        fields = ('id', 'username', 'email', 'is_active', 'is_staff')
        read_only_fields = ('id',)
        extra_kwargs = {
            'username': {'required': True, 'max_length': 150},
            'email': {'required': True, 'max_length': 254},
            'is_active': {'default': True},
            'is_staff': {'default': False}
        }

