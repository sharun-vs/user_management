from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ListUsersApi

router = DefaultRouter()

router.register('listusers', ListUsersApi, basename='list users')

urlpatterns = [
    url(r'^', include(router.urls)),
 ]