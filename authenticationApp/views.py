from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .handler import handle_uploaded_file


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})

from django.shortcuts import redirect
from django.http import HttpResponse

def UploadSucc(request):
    return HttpResponse("FILE UPLOAD SUCCESSFULLY")

from .forms import ModelFormWithFileField

def upload_fileWModel(request):
    if request.method == "POST":
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/success/url/")
    else:
        form = ModelFormWithFileField()
    return render(request, "upload.html", {"form": form})





