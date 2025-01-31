from django.contrib import admin
from django.urls import path,include
from . import views

app_name='accounts'
urlpatterns = [
    
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name='profile'),
    path('blogs/',views.profile_blogs,name='profile_blogs'),
    path('edit-profile/',views.edit_profile,name="edit_profile"),
    path('publish/<int:blog_id>/',views.publish_now,name='publish_now'),
    

]