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


class Image(models.Model):
    name = models.ForeignKey(Page)
    image = models.ImageField(upload_to='slider_image/', unique=True)


class Video(models.Model):
    name = models.ForeignKey(Page)
    url = models.URLField()
    image = models.ImageField(upload_to='upload/', unique=True)

    def __str__(self):
        return self.name.page_name


class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(Workshop)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('workshop', 'email')


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EventRegistration(models.Model):
    BRANCH_CHOICES = ((None,'----'),
    ('MCA', 'MCA'), ('MBA', 'MBA'), ('CS', 'CS'), ('IT', 'IT'),
    ('ECE', 'ECE'), ('EN', 'EN'), ('ME', 'ME'),('EI','EI'),('CE','CE'))
    YEAR_CHOICES=((0,'----'),(1,'1'),(2,'2'),(3,'3'),(4,'4'))
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    student_no = models.CharField(default=None,null=True,max_length=10)
    branch = models.CharField(choices=BRANCH_CHOICES,default=None,max_length=3,null=True)
    year=models.IntegerField(choices=YEAR_CHOICES,default=None,null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('event', 'email')
