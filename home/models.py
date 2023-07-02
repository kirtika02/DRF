from django.db import models
import uuid
from uuid import uuid4
import os


# Create your models here.

class Folder(models.Model): #creating a folder to store the files
    uid = models.UUIDField(primary_key= True , editable= False , default=uuid4) #unique id for each file... would be called automatically
    created_at=models.DateField(auto_now=True)

def get_upload_path(instance, filename):#creates a random folder and puts the file in it
    return os.path.join(str(instance.folder.uid),filename)

class Files(models.Model): #creating a file class
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE) # folder created from folder class
    file = models.FileField(upload_to=get_upload_path)   #dumps the files onto the folder after the folder is created dynamically
    created_at=models.DateField(auto_now=True)

