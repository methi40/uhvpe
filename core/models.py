from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Page(models.Model):
    page_name = models.CharField(max_length=50)
    content = RichTextUploadingField()

    def __str__(self):
        return self.page_name

class Workshop(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

