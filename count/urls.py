from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.Register.as_view(), name='register'),
    path('controlPanel/', views.control, name="controlPanel"),
    path('roomList/',views.roomList, name="roomList"),
    path('addRoom/<int:org>', views.AddRoom.as_view(), name='addRoom'),
    path('editRoom/<int:pk>', views.EditRoom.as_view(), name='editRoom'),
    path('deleteRoom/<int:pk>', views.DeleteRoom.as_view(), name='deleteRoom'),
    path('addUser/<int:org>', views.AddUser.as_view(), name='addUser'),
    path('editUser/<int:pk>', views.EditUser.as_view(), name='editUser'),
    path('deleteUser/<int:pk>', views.DeleteUser.as_view(), name='deleteUser'),
    path('count/<int:r>', views.count, name='count'),
    path('addAdmin', views.AddAdminUser.as_view(), name="addAdmin"),
    
]