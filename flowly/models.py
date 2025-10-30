from django.db import models
from django.contrib.auth.models import User



class Message(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response_to=models.ForeignKey('self',on_delete=models.PROTECT, null=True,related_name='responses')
#related_name='responses'
