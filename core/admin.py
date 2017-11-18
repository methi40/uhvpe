from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import (Page, Workshop, Presentation, SliderImage, QuestionPaper, Note, PracticeSession,
                     Circular, Poster, VideoLecture, WorkshopRegistration)


class WorkshopRegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'workshop')
    search_fields = ('name',)


# Register your models here.
admin.site.register(Page)
admin.site.register(Workshop)
admin.site.register(Presentation)
admin.site.register(SliderImage)
admin.site.register(QuestionPaper)
admin.site.register(Note)
admin.site.register(PracticeSession)
admin.site.register(Circular)
admin.site.register(Poster)
admin.site.register(VideoLecture)
admin.site.register(WorkshopRegistration, WorkshopRegistrationAdmin)
