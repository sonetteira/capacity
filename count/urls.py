from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.Register.as_view(), name='register'),
    path('addRoom', views.AddRoom.as_view(), name='addRoom'),
    path('count/<int:r>', views.count, name='count'),
    path('addAdmin/<int:org>', views.AddAdminUser.as_view(), name="addAdmin"),
]