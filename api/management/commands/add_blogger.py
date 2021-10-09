from django.core.management.base import BaseCommand
from ...models import InstaBlogger

class Command(BaseCommand):
	help = 'Adding bloggers. Use with blogger login as arg'

	def add_arguments(self, parser):
		parser.add_argument('blogger', type=str, help='blogger_login')

	def handle(self, *args, **kwargs):
		blogger_login = kwargs['blogger']
		if not InstaBlogger.objects.filter(blogger_name = blogger_login).exists():
			blogger = InstaBlogger()
			blogger.blogger_name = blogger_login
			blogger.save()
