from django.contrib import admin
from sharing.models import AuthToken

class AuthTokenAdmin(admin.ModelAdmin):
	fields = ['token','directory','expiration','note']
	list_display = ('token','expiration','note')

admin.site.register(AuthToken,AuthTokenAdmin)
