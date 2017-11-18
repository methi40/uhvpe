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
    description = RichTextUploadingField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Presentation(models.Model):
    HINDI = 'HI'
    ENGLISH = 'EN'
    LANGUAGE_CHOICES = ((HINDI, 'Hindi'), (ENGLISH, 'English'))
    name = models.CharField(max_length=50, unique=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    file = models.FileField(upload_to='presentation/', unique=True)

    def __str__(self):
        return self.name


class Circular(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='circular/', unique=True)

    def __str__(self):
        return self.name


class PracticeSession(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='practice_session/', unique=True)

    def __str__(self):
        return self.name


class Poster(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='poster/', unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='note/', unique=True)

    def __str__(self):
        return self.name


class QuestionPaper(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='question_paper/', unique=True)

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_image/', unique=True)


class VideoLecture(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(Workshop)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('workshop', 'email')
