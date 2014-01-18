# encoding=utf-8

from django.contrib import admin
from pubkey.models import PublicKey, Server


admin.site.register(Server, admin.ModelAdmin)
admin.site.register(PublicKey, admin.ModelAdmin)

