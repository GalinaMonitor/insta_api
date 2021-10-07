from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
	path('insta_users/', views.InstaUserList.as_view(), name='user_list'),
	path('insta_users/<int:pk>/', views.InstaUserDetail.as_view(), name='user_detail'),
	path('bloggers/', views.InstaBloggerList.as_view(), name='blogger_list'),
	path('bloggers/<int:id>/', views.InstaBloggerDetail.as_view(), name='blogger_detail'),
	path('intersect/', views.Intersections.as_view()),
	path('getlogin/<int:id>/', views.GetNameInstaUser.as_view()),
	path('', views.Help.as_view())
]

