from django.core.management.base import BaseCommand
from ...models import InstaBlogger

class Command(BaseCommand):
	def handle(self, *args, **options):
		if not InstaBlogger.objects.filter(blogger_name = 'katyushka_tyan').exists():
			blogger = InstaBlogger()
			blogger.blogger_name = 'katyushka_tyan'
			blogger.save()
		if not InstaBlogger.objects.filter(blogger_name = 'dima_gordey').exists():
			blogger = InstaBlogger()
			blogger.blogger_name = 'dima_gordey'
			blogger.save()
