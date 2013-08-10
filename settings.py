from django.conf import settings

SHARING_DIRECTORY=getattr(settings, 'SHARING_DIRECTORY', u"sharing/shares")
SHARING_TIMES = getattr(settings, 'SHARING_TIMES', {
	60*60:'1 hour',
	4*60*60:'4 hours',
	24*60*60:'1 day',
	2*24*60*60:'2 days',
	7*24*60*60:'7 days',
	30*24*60*60:'30 days',
	365*24*60*60:'1 year'
})
	
