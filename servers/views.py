from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Server
from django.contrib.auth.decorators import login_required

def default_app_page(request):
    return HttpResponse("Default app page") 

def server_list(request):
    servers = Server.objects.all()
    return render(request, 'servers/server_list.html', {'servers':servers})

def server_detail(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    return render(request, 'servers/server_detail.html', {'server':server})

@login_required
def secure_page(request):
    return render(request, 'servers/secure.html', {'user': request.user})


# Create your views here.
