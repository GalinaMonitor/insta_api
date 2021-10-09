from django.core.management.base import BaseCommand
from instabot import Bot
from ...models import InstaBlogger, InstaUser

class Command(BaseCommand):
	help = 'Update base for all bloggers'

	def handle(self, *args, **options):
		bot = Bot()
		bot.login(username = "",  password = "", proxy='', use_cookie = False)
		bloggers = InstaBlogger.objects.all()
		for blogger in bloggers:
			blogger_followers = bot.get_user_followers(blogger.blogger_name)
			for follower in blogger_followers:
				if not InstaUser.objects.filter(user_id = follower).exists():
					user = InstaUser()
					user.user_id = follower
					user.user_follower = blogger.blogger_name
					user.user_login = bot.get_username_from_user_id(follower)
					user.save()
