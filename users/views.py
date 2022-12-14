from django.contrib.auth import authenticate
from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'message': "User created successfully!!!",
                'data': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request: Request):
        phone = request.data.get("phone")
        password = request.data.get("password")

        user = authenticate(phone=phone, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login Successfully!",
                "tokens": tokens
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(data={'message': "Invalid phone or password"})

    def get(self, request: Request):
        response = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(response, status=status.HTTP_200_OK)