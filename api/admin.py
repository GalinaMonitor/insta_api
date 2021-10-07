from django.contrib import admin
from api.models import InstaBlogger, InstaUser

@admin.register(InstaUser)
class PostAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'user_follower')
	raw_id_fields = ('user_follower',)
	list_filter = ('user_follower', 'updated')

@admin.register(InstaBlogger)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'blogger_name')

