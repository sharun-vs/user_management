from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import UpdateUserApi

router = DefaultRouter()

router.register('updateuser', UpdateUserApi, basename='update user')

urlpatterns = [
    url(r'^', include(router.urls)),
 ]