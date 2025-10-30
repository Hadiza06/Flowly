from django.contrib import admin
from flowly.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'user')
    #list_filter = ('user',)


admin.site.register(Message)
