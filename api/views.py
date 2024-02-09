from django.shortcuts import render
from . import views
from .models import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
def upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for file in files:
            file_obj = File(file=file)
            file_obj.save()
    return render(request,'api/upload.html')

def list(request):
    files = File.objects.all()
    content =""
   
    for file_obj in files:
        link = f"https://automaton-project.onrender.com/download/{file_obj.id}\n"
        content+=link
        

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'inline; filename=links.txt'
    return response 

def download(request, id):
    file = get_object_or_404(File, pk=id)
    response = FileResponse(file.file, as_attachment=True)
    
    
    file.delete()
    return response
