from django.shortcuts import render
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Signup(APIView):
    def post(self, request, format=None):
        serializers = CustomUserSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializers.data}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"User not found"}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
            return Response({"error": "Invalid credentials, please try again"}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        serializer = CustomUserSerializer(user)
        user_data = serializer.data
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user": user_data, "message": "User logged in successfully"}, status=status.HTTP_200_OK)

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            return Response(
                {"error": "Invalid token or already logged out."},
                status=status.HTTP_400_BAD_REQUEST
            )
        Logout(request)

        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK) 