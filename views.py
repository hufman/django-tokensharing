from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.views.static import serve as serve_static

from . import files
from . import tokens
from . import settings

def index(request):
	return HttpResponse("Hello")

@login_required
def admin(request, root):
	if not files.is_directory(root) and not files.is_file(root):
		raise Http404()
	if not files.is_directory(root):
		return download(request, root)
	if request.method == 'POST':
		return generate_token(request,root)
	expirations = [{'secs':k, 'name':v} for k,v in settings.SHARING_TIMES.items()]
	expirations.sort(key=lambda x:x['secs'])
	vars = {"loggedin":True, "expirations":expirations}
	if root!='' and root!='/':
		vars['parent'] = '..'
	return browse(request,root,vars)

def sub(request, root, token, sub):
	if not tokens.validate(root, token):
		raise Http404()
	url = root+'/'+sub
	if not files.is_directory(url):
		return download(request, url)
	vars = {}
	if sub!='' and sub!='/':
		vars['parent'] = '..'
	return browse(request, url, vars)
	
def generate_token(request,root):
	token = tokens.generate_new(root, int(request.POST['expiration']), request.POST['note'])
	template = get_template('success.djhtml')
	context = Context({'token':token,'root':root,'note':request.POST['note']})
	context['url'] = ':'+token
	if files.is_directory(root):
		context['url'] += '/'
	return HttpResponse(template.render(context))
def browse(request,root,vars):
	contents = files.get_directory_contents(root)
	for content in contents:
		if content['isdir']:
			content['url'] = content['name']+"/"
		else:
			content['url'] = content['name']
	template = get_template('browse.djhtml')
	context = RequestContext(request,vars)
	context['contents'] = contents
	return HttpResponse(template.render(context))

def download(request,path):
	return serve_static(request, path, settings.SHARING_DIRECTORY)
