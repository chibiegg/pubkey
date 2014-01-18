# encoding=utf-8

from django.db import models

from django.contrib.auth.models import User

class Server(models.Model):

    user = models.ForeignKey(User)
    description = models.CharField(u"名称", max_length=255)
    hostname = models.CharField(u"ホスト名", max_length=255)
    apikey = models.CharField(u"APIKey", max_length=100)
    
    
    def __unicode__(self):
        return self.description

class PublicKey(models.Model):

    user = models.ForeignKey(User)
    server = models.ForeignKey("Server", null=True, blank=True)
    key = models.TextField(u"公開鍵")
    description = models.CharField(u"名称", max_length=255)

    def __unicode__(self):
        return self.description

