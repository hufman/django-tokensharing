import datetime
import hashlib
import base64
from . import models
from django.conf import settings
from django.utils.timezone import now

def generate_new(directory, expiration_seconds, note):
	time = now()
	scoot = datetime.timedelta(seconds=expiration_seconds)
	expiration = time + scoot
	token = models.AuthToken(directory=directory, expiration=expiration, note=note)
	hasher = hashlib.sha1()
	hasher.update(settings.SECRET_KEY)
	hasher.update(directory)
	hasher.update(expiration.isoformat())
	hmac = hasher.digest()
	token.token = urlencode(hmac)
	token.save()
	return token.token
def validate(directory, token):
	matches = models.AuthToken.objects.filter(token=token).filter(directory=directory).filter(expiration__gte=now())
	return len(matches)>0
	
def urlencode(token):
	b64 = base64.urlsafe_b64encode(token)
	b64 = b64.replace('=','.')
	return b64
def urldecode(b64):
	b64 = b64.replace('.','=')
	token = base64.urlsafe_b64decode(token)
	return token
