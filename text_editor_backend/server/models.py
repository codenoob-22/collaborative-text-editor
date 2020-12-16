from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.



class Document(models.Model):
    users           = models.ManyToManyField(User, related_name='documents')
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='own_documents')
    version         = models.BigIntegerField(default=0)
    last_updated    = models.DateTimeField(auto_now_add=True)
    pub_date        = models.DateTimeField(auto_now_add=True)
    body            = RichTextField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
