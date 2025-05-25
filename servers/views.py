from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Server
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServerListSerializer, ServerDetailSerializer
from django.shortcuts import redirect
import csv
import os
from django.conf import settings
from django.views.decorators.http import require_POST
from django.contrib import messages

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

def server_list(request):
    server_id = request.GET.get("server_id")
    if server_id:
        return redirect('server_detail', server_id=server_id)

    servers = Server.objects.all()
    return render(request, 'servers/server_list.html', {'servers': servers})

@api_view(['GET'])
def server_detail_api(request, pk):
    try:
        server = Server.objects.get(pk=pk)
    except Server.DoesNotExist:
        return Response({"error": "Server not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServerDetailSerializer(server)
    return Response(serializer.data)

@api_view(['POST'])
def server_create_api(request):
    serializer = ServerDetailSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

CSV_FILE_PATH = os.path.join(settings.BASE_DIR, 'uploaded_servers.csv')

def csv_view(request):
    
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.lower().endswith('.csv'):
            return HttpResponse("File is not CSV type", status=400)
        
        with open(CSV_FILE_PATH, 'wb+') as destination:
            for chunk in csv_file.chunks():
                destination.write(chunk)
        
        return redirect('csv_view')

    # GET
    rows = []
    if os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    
    return render(request, 'servers/csv_view.html', {'rows': rows})

@require_POST
def csv_delete(request):
    if os.path.exists(CSV_FILE_PATH):
        os.remove(CSV_FILE_PATH)
    return redirect('csv_view')

@login_required
def delete_server(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    server.delete()
    messages.success(request, f"Server '{server.name}' delete")
    return redirect('server_list')

# Create your views here.
