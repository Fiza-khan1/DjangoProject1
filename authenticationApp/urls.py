from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.upload_file,name='upload'),
    path('success/',views.UploadSucc,name='success'),
    path('upload_file/',views.upload_fileWModel,name='uploadfile')

]
