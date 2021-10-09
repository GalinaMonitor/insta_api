from django.core.management.base import BaseCommand
from instabot import Bot
from ...models import InstaUser

class Command(BaseCommand):
	def handle(self, *args, **options):
		bot = Bot()
		bot.login(username = "",  password = "", proxy='', use_cookie = False)
		user_followers = bot.get_user_followers('dmitriy.sa')
		for follower in user_followers:
			if not InstaUser.objects.filter(user_id = follower).exists():
				user = InstaUser()
				user.user_id = follower
				user.user_follower = 'katyushka_tyan'
				user.user_login = bot.get_username_from_user_id(follower)
				user.save()
		user_followers = bot.get_user_followers('dmitriy.sa')
		for follower in user_followers:
			if not InstaUser.objects.filter(user_id = follower).exists():
				user = InstaUser()
				user.user_id = follower
				user.user_follower = 'dima_gordey'
				user.user_login = bot.get_username_from_user_id(follower)
				user.save()
