from django.shortcuts import render
from django.views.generic import View
from .models import Page


# Create your views here.
class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Home').first()
        return render(request, self.template_name, context={'page': page})


class DirectorMessageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Director Message').first()
        return render(request, self.template_name, context={'page': page})


class UHVPESyllabus(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='UHVPE Syllabus').first()
        return render(request, self.template_name, context={'page': page})


class GuidelineView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='UHVPE Guidelines').first()
        return render(request, self.template_name, context={'page': page})


class SociallyRelevantProjectView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Socially Relevant Projects').first()
        return render(request, self.template_name, context={'page': page})


class BookView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Books').first()
        return render(request, self.template_name, context={'page': page})


class FAQView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='FAQ').first()
        return render(request, self.template_name, context={'page': page})


class JourneySoFarView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Journey So Far').first()
        return render(request, self.template_name, context={'page': page})


class ImpactView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Impact').first()
        return render(request, self.template_name, context={'page': page})


class FuturePlansView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Future Plans').first()
        return render(request, self.template_name, context={'page': page})


class NodalCenterView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Nodal Centers').first()
        return render(request, self.template_name, context={'page': page})
