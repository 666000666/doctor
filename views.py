
from django.htttp import HttpResponse

def index(request):
    return HttpResponse('index')
def login(request):
    rediect('/index')
