from django.urls import include, path
from django.contrib import admin

from waterGIS.views import login_user
from .views import *
from django.urls import path

urlpatterns = [

    path('login/', login_user, name='login'),

    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile'),

    path('change_profile_picture/', change_profile_picture,
         name='change_profile_picture'),
    path('view_user_information/<str:username>/',
         view_user_information, name="view_user_information"),

    # your other urls
    path('request_premium_access/', request_premium_access,
         name='request_premium_access'),
    path('some_view/', some_view, name='some_view'),
    path('get_user_permission_status/', get_user_permission_status, name='get_user_permission_status'),
]



    # add your other paths here

