from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=13)
    first_name = serializers.CharField(min_length=100)
    last_name = serializers.CharField(min_length=100)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = 'username phone first_name last_name password password2'.split()

    def validate_phone(self, phone):
        if len(phone) < 13:
            raise ValidationError("Not enough numbers!")
        elif phone[:4] != '+996':
            raise ValidationError("Number must start with +996!")
        elif not phone[1:].isdigit():
            raise ValidationError("Number must contain only digits!")

        return phone


    def create(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password2 != password:
            raise ValidationError({password: "Passwords not match"})

        user.set_password(password)
        user.save()
        return user