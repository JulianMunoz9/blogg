from django.urls import path
from . import views
from .views import post_list

urlpatterns = [
    path('', views.home, name="home"),
    path('post_list/', views.PostListView.as_view(), name="Post_list"),
    path('post_detail/', views.PostListView.as_view(), name="Post_detail")
    
    
]