from rest_framework import viewsets
from .serializer import UserListSerializer
from user.models import User

class ListUsersApi(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.filter(is_admin=False)
    print(queryset)