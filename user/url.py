from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import UserSignUpApi, AdminSignUpApi, LoginApi

router = DefaultRouter()

router.register('signup', UserSignUpApi, basename='user sign up')
router.register('admin', AdminSignUpApi, basename='admin sign up')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', LoginApi.as_view(), name='login'),
    ]