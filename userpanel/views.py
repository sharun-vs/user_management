from rest_framework import viewsets
from .serializer import EditUserSerializer
from rest_framework.response import Response

class UpdateUserApi(viewsets.ViewSet):
	serializer_class = EditUserSerializer
	def update(self, pk):
		user = User.objects.get(id=pk)
		serializer = self.serializer_class(user, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({"msg":"user updated successfully", "data":serializer.data})