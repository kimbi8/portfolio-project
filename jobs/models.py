from django.db import models

class Job(models.Model): # object get saved into the database through models.Model?
    image = models.ImageField(upload_to = 'images/') #tells where image will be saved
    summary = models.CharField(max_length = 200)
    
