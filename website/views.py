from django.http import HttpResponse
from django.template import loader
from .models import Users

def index(request):
    all_users = Users.objects.all()
    template = loader.get_template('website/index.html')
    context = {
        'all_users' : all_users,
    }
    return HttpResponse(template.render(context, request))
