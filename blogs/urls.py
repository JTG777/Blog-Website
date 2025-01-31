from django.contrib import admin
from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    
    path('',views.index,name="index"),
    path('add-post/',views.add_post,name='add_post'),
    path('view-post/<slug:slug>/',views.view_post,name='view_post'),
    path('edit-post/<int:blog_id>/',views.edit_post,name='edit_post'),
    path('delete-post/<int:blog_id>',views.delete_post,name='delete_post'),
    path('category/<slug:slug>/',views.view_category_post,name='view_category_post'),
    path('like-post/<int:blog_id>/',views.like_post,name='like_post'),
    # path('search/',views.nav_search,name='nav_search'),
]