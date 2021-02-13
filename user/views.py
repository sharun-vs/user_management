from rest_framework import viewsets
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User

class AdminSignUpApi(viewsets.ViewSet):
	serializer_class = UserSerializer

	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(is_admin=True)
		return Response({"msg":"admin created successfully","data":serializer.data})

class UserSignUpApi(viewsets.ViewSet):
	serializer_class = UserSerializer

	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"msg":"account created successfully","data":serializer.data})

class LoginApi(APIView):
	
	def post(self, request):
		user = User.objects.get(email=request.data['email'])
		if request.data['email']==user.email and request.data['password'] == user.password:
			serializer = UserSerializer(user)
			return Response({"msg":"user logged in","data":serializer.data})
		else:
			return Response({"msg":"user does not exists"})