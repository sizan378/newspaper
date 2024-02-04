from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class UserLoginView(TokenObtainPairView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response(
                {"message": "Please provide email and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        User = get_user_model()

        try:
            user_exists_check = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(password, user_exists_check.password):
            return Response(
                {"message": "Password is incorrect"}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer_class = MyTokenObtainPairSerializer
        # Generate token using serializer class
        serializer = serializer_class(data={"email": email, "password": password})
        if serializer.is_valid():
            # Token generation
            token = serializer.validated_data
            return Response(
                {"access_token": token["access"], "refresh_token": token["refresh"]}
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
