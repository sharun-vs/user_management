from rest_framework import serializers
from user.models import User

class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model =User
		fields = ['id','username', 'full_name', 'email']