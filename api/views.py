from rest_framework import generics
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InstaUser, InstaBlogger
from instabot import Bot

class Intersections(APIView):
	def get(self, request, blogger1, blogger2):
		blogger1 = get_object_or_404(InstaBlogger, blogger_name=blogger1)
		blogger2 = get_object_or_404(InstaBlogger, blogger_name=blogger2)
		queryset3 = InstaUser.objects.values_list('user_id').filter(user_follower = blogger1.id)
		queryset4 = InstaUser.objects.values_list('user_id').filter(user_follower = blogger2.id)
		result = queryset3.intersection(queryset4)
		result1 = InstaUser.objects.none()
		for id in result:
			result1 = result1 | InstaUser.objects.filter(user_id = id[0])[:1]
			print(result1)
		return Response(result1.values('id', 'user_id'))

class GetNameInstaUser(APIView):
	def get(self, request, id, format=None):
		user = get_object_or_404(InstaUser, id=id)
		serializer = serializers.InstaUserSerializer(user)
		return Response({'data' : serializer.data, 'login' : user.user_login})

class Help(APIView):
	def get(self, request):
		return Response({'User list' : '/users',
						'Blogger list' : '/bloggers',
						'Blogger_followers' : '/bloggers/<id>',
						'Intersections' : '/intersect/<blogger_name1>/<blogger_name2>',
						'Get User Login' : '/getlogin/<id>'})

class InstaUserList(generics.ListAPIView):
	queryset = InstaUser.objects.all()
	serializer_class = serializers.InstaUserSerializer

class InstaUserDetail(generics.RetrieveAPIView):
	queryset = InstaUser.objects.all()
	serializer_class = serializers.InstaUserFullSerializer

class InstaBloggerList(generics.ListAPIView):
	queryset = InstaBlogger.objects.all()
	serializer_class = serializers.InstaBloggerSerializer

class InstaBloggerDetail(APIView):
	def get(self, request, id, format=None):
		queryset = InstaUser.objects.filter(user_follower = id)
		serializer = serializers.InstaUserSerializer(queryset, many=True)
		return Response({'followers' : serializer.data})

