from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register/<int:usr>', views.Register.as_view(), name='register'),
    path('addRoom', views.AddRoom.as_view(), name='addRoom'),
    path('count/<int:r>', views.count, name='count'),
    path('addAdmin', views.AddAdminUser.as_view(), name="addAdmin"),
    path('controlPanel/', views.control, name="controlPanel"),
]