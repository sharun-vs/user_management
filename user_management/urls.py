from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.url')),
    path('userpanel/', include('userpanel.url')),
    path('adminpanel/', include('adminpanel.url')),
]