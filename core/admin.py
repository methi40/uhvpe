from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import (Page, Workshop, Presentation, SliderImage, QuestionPaper, Note, PracticeSession,
                     Circular, Poster, VideoLecture, WorkshopRegistration, Event, EventRegistration)


class WorkshopRegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'workshop')
    search_fields = ('name', 'email')
    list_filter = ('workshop',)


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class EventRegistrationAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'phone', 'event')
    search_fields = ('name', 'email')
    list_filter = ('event',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


# Register your models here.
admin.site.register(Page)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Presentation)
admin.site.register(SliderImage)
admin.site.register(QuestionPaper)
admin.site.register(Note)
admin.site.register(PracticeSession)
admin.site.register(Circular)
admin.site.register(Poster)
admin.site.register(VideoLecture)
admin.site.register(WorkshopRegistration, WorkshopRegistrationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
