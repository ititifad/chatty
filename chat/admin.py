from django.contrib import admin
from chat.models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['username', 'room', 'content','date_added']
    list_filter = ['room', 'username']
