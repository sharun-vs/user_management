from rest_framework import serializers
from user.models import User

class EditUserSerializer(serializers.ModelSerializer):
	date_of_birth = serializers.DateField()
	address = serializers.CharField(max_length=255)
	profile_image = serializers.ImageField(max_length=None, allow_empty_file=True)
	id_proof = serializers.FileField(max_length=None, allow_empty_file=False)

	class Meta:
		model = User
		fields = ['username', 'full_name', 'email', 'date_of_birth', 'address', 'profile_image', 'id_proof']