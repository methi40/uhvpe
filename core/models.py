from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

choices = (('Left', 'Left'),
           ('Right', 'Right'),
           ('None', 'None'))

class Page(models.Model):
    page_name = models.CharField(max_length=50)
    content = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.page_name


class Workshop(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField(blank=True)
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


class Files(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='note/', unique=True)

    def __str__(self):
        return self.page.page_name + "-" + self.name


class QuestionPaper(models.Model):
    name = models.CharField(max_length=50, unique=True)
    file = models.FileField(upload_to='question_paper/', unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=25, default='')
    image = models.ImageField(upload_to='slider_image/', unique=True)

    def __str__(self):
        return self.page.page_name + "-" + self.name

class Image_Slider(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to='home_slider/',unique=True)

    def __str__(self):
        return self.page.page_name+"-"+self.name


class Charts(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    text = models.CharField(max_length=500, unique=True)
    number_of_values = models.BigIntegerField()
    values = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.page.page_name + " - " + self.text

    def clean(self, *args, **kwargs):
        number = self.values.split(',')
        if((len(number)/2) == int(self.number_of_values)):
            super(Charts, self).clean(*args, **kwargs)
        else:
            raise ValidationError(u'Number of values provided incorrectly in field!')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Charts, self).save(*args, **kwargs)

class Video(models.Model):
    page = models.ForeignKey(Page,on_delete=models.CASCADE)
    url = models.URLField()
    position = models.CharField(max_length=50, choices=choices, blank=False)
    video_name = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.page.page_name + "-" + self.video_name


class WorkshopRegistration(models.Model):
    workshop = models.ForeignKey(Workshop,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('workshop', 'email')


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField(blank=True)
    active = models.BooleanField(default=False)
    new_event = models.BooleanField(default=False)
    date = models.DateField(("Date"), default=date.today)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class EventRegistration(models.Model):
    BRANCH_CHOICES = ((None,'----'),
    ('MCA', 'MCA'), ('MBA', 'MBA'), ('CS', 'CS'), ('IT', 'IT'),
    ('ECE', 'ECE'), ('EN', 'EN'), ('ME', 'ME'),('EI','EI'),('CE','CE'))
    YEAR_CHOICES=((0,'----'),(1,'1'),(2,'2'),(3,'3'),(4,'4'))
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
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

class Notification(models.Model):
    name = models.CharField(max_length=200)
    new_notification = models.BooleanField(default=False)

    def __str__(self):
        return self.name
