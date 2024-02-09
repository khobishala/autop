from django.shortcuts import render
from . import views
from .models import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        for file in files:
            file_obj = File(file=file)
            file_obj.save()
    return render(request,'api/upload.html')

def list(request):
    return render(request,"api/list.html",{
        'files':File.objects.all()
    })

def download(request, id):
    file = get_object_or_404(File, pk=id)
    response = FileResponse(file.file, as_attachment=True)
    file.delete()
    return response
