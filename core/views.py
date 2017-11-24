from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from .forms import WorkshopRegistrationForm, EventRegistrationForm
from .models import Page, SliderImage, Presentation, Circular, PracticeSession, Poster, Note, QuestionPaper, \
    VideoLecture, Workshop, WorkshopRegistration, EventRegistration, Event


# Create your views here.
def slider_image():
    return SliderImage.objects.all()


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Home').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class DirectorMessageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Director Message').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class UHVPESyllabus(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='UHVPE Syllabus').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class GuidelineView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='UHVPE Guidelines').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class SociallyRelevantProjectView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Socially Relevant Projects').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class BookView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Books').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class FAQView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='FAQ').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class JourneySoFarView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Journey So Far').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class ImpactView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Impact').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class FuturePlansView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Future Plans').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class NodalCenterView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Nodal Centers').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class ContactView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Contact').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class PastWorkshopDetailView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Past Workshop Detail').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class UHVPEProgramView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='UHVPE Program').first()
        return render(request, self.template_name, context={'page': page, 'slider_image': slider_image()})


class PresentationView(ListView):
    model = Presentation
    template_name = 'index.html'
    extra_context = {'table_name': 'Presentation', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(PresentationView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class PosterView(ListView):
    model = Poster
    template_name = 'index.html'
    extra_context = {'table_name': 'Posters', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(PosterView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class CircularView(ListView):
    model = Circular
    template_name = 'index.html'
    extra_context = {'table_name': 'Circulars', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(CircularView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class PracticeSessionView(ListView):
    model = PracticeSession
    template_name = 'index.html'
    extra_context = {'table_name': 'Practice Sessions', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(PracticeSessionView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class NoteView(ListView):
    model = Note
    template_name = 'index.html'
    extra_context = {'table_name': 'Notes', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(NoteView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class QuestionPaperView(ListView):
    model = QuestionPaper
    template_name = 'index.html'
    extra_context = {'table_name': 'Question Papers', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(QuestionPaperView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class VideoLectureView(ListView):
    model = VideoLecture
    template_name = 'index.html'
    extra_context = {'table_name': 'Video Lectures', 'slider_image': slider_image()}

    def get_context_data(self, **kwargs):
        context = super(VideoLectureView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class WorkshopRegistrationView(View):
    template_name = "workshop_registration.html"
    form = WorkshopRegistrationForm

    def get(self, request, *args, **kwargs):
        workshops = Workshop.objects.filter(active=True)
        return render(request, self.template_name, context={'workshops': workshops, 'form': WorkshopRegistrationForm,
                                                            'slider_image': slider_image()})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not Workshop.objects.filter(id=request.POST['workshop'], active=True).exists():
            messages.error(request, "The registration for this workshop is not active.")
        elif WorkshopRegistration.objects.filter(workshop=request.POST['workshop'],
                                                 email=request.POST['email']).exists():
            messages.error(request, "This email is already registered for this workshop.")
        elif form.is_valid():

            new_registration = form.save(commit=False)
            new_registration.workshop = Workshop.objects.get(id=request.POST['workshop'], active=True)
            messages.success(request, "You have successfully registered.")
            form.save()
        else:
            messages.error(request, "Enter correct values in all the fields.")
        return HttpResponseRedirect(reverse('workshop'))


class EventRegistrationView(View):
    template_name = "event_registration.html"
    form = EventRegistrationForm

    def get(self, request, *args, **kwargs):
        events = Event.objects.filter(active=True)
        return render(request, self.template_name, context={'events': events, 'form': EventRegistrationForm,
                                                            'slider_image': slider_image()})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not Workshop.objects.filter(id=request.POST['event'], active=True).exists():
            messages.error(request, "The registration for this event is not active.")
        elif EventRegistration.objects.filter(event=request.POST['event'], email=request.POST['email']).exists():
            messages.error(request, "This email is already registered for this event.")
        elif form.is_valid():

            new_registration = form.save(commit=False)
            new_registration.event = Event.objects.get(id=request.POST['event'], active=True)
            messages.success(request, "You have successfully registered.")
            form.save()
        else:
            messages.error(request, "Enter correct values in all the fields.")
        return HttpResponseRedirect(reverse('event'))
