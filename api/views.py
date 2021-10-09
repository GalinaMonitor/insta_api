from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InstaUser, InstaBlogger
from instabot import Bot

# INFO
class Help(APIView):
	def get(self, request):
		return Response({'User list' : '/users',
						'Blogger list' : '/bloggers',
						'Blogger_followers' : '/bloggers/<blogger_name>',
						'Intersections' : '/intersect/<blogger_name1>/<blogger_name2>',
						'Get User Login' : '/getlogin/<id>'})

class Intersections(APIView):
	def get(self, request, blogger1, blogger2):
		blogger1 = get_object_or_404(InstaBlogger, blogger_name=blogger1)
		blogger2 = get_object_or_404(InstaBlogger, blogger_name=blogger2)
		queryset1 = InstaUser.objects.values_list('user_id').filter(user_follower = blogger1.id)
		queryset2 = InstaUser.objects.values_list('user_id').filter(user_follower = blogger2.id)
		result = queryset1.intersection(queryset2)
		list_of_users = InstaUser.objects.none()
		for id in result:
			list_of_users = list_of_users | InstaUser.objects.filter(user_id = id[0])[:1]
		return Response(list_of_users.values('id', 'user_id'))

# Special view and serializer for user_login(Just for security)
class GetNameInstaUser(APIView):
	def get(self, request, id, format=None):
		user = get_object_or_404(InstaUser, id=id)
		serializer = serializers.InstaUserSerializer(user)
		return Response({'data' : serializer.data, 'login' : user.user_login})

# Blogger name, number of followers and a list of followers
class InstaBloggerDetail(APIView):
	def get(self, request, blogger, format=None):
		blogger = get_object_or_404(InstaBlogger, blogger_name=blogger)
		queryset = InstaUser.objects.filter(user_follower = blogger.id)
		serializer = serializers.InstaUserSerializer(queryset, many=True)
		return Response({'followers_number' : queryset.count(), 'followers' : serializer.data})

class InstaUserList(generics.ListAPIView):
	queryset = InstaUser.objects.all()
	serializer_class = serializers.InstaUserSerializer

class InstaUserDetail(generics.RetrieveAPIView):
	queryset = InstaUser.objects.all()
	serializer_class = serializers.InstaUserFullSerializer

class InstaBloggerList(generics.ListAPIView):
	queryset = InstaBlogger.objects.all()
	serializer_class = serializers.InstaBloggerSerializer
