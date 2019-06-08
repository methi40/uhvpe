from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from .forms import WorkshopRegistrationForm, EventRegistrationForm
from .models import Page, Image, Presentation, Circular, PracticeSession, Poster, Files, QuestionPaper, \
    Video, Workshop, WorkshopRegistration, EventRegistration, Event, Charts
from uhvpe.settings.base import RECAPTCHA_PUBLIC_KEY, RECEIVER_EMAIL, EMAIL_HOST_USER

import json



# Create your views here.


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        page = Page.objects.filter(page_name='Home').first()
        # slider_images = Image.objects.filter(page=page, name__icontains='slider')
        videos_left = Video.objects.filter(page=page, position='Left')
        videos_right = Video.objects.filter(page=page, position='Right')
        images = Image.objects.filter(page=page)
        print(images)
        key = RECAPTCHA_PUBLIC_KEY
        return render(request, self.template_name, context={'videos_left':videos_left, 'videos_right':videos_right,
                                                            'images':images,'key':key})


class DirectorMessageView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Director Message </h3></div>"
        page = Page.objects.filter(page_name='Director Message').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class VisionAndMissionView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class='my-2' ><span class='about-us'>Vision & Mission</span></h3></div>"
        page = Page.objects.filter(page_name='Vision And Mission').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class EstablishmentView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Establishment</span> </h3></div>"
        page = Page.objects.filter(page_name='Establishment').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class StructureView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Structure</span> </h3></div>"
        page = Page.objects.filter(page_name='Structure').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class SyllabusView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Syllabus</span> </h3></div>"
        page = Page.objects.filter(page_name='Syllabus').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class BookAndAuthorsView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Book And Authors</span></h3></div>"
        page = Page.objects.filter(page_name='Book And Authors').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class UnitWiseNotesView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Unit Wise Notes</span> </h3></div>"
        page = Page.objects.filter(page_name='Unit Wise Notes').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class VideoLecturesView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Video Lectures</span> </h3></div>"
        page = Page.objects.filter(page_name='Video Lectures').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        videos = Video.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images, 'videos':videos})

class UnitWisePPTView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Unit Wise PPT</span> </h3></div>"
        page = Page.objects.filter(page_name='Unit Wise PPT').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class UTQuestionPaperView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>UT Question Paper</span> </h3></div>"
        page = Page.objects.filter(page_name='UT Question Paper').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class PreviousPaperView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Previous Year Papers</span> </h3></div>"
        page = Page.objects.filter(page_name='Previous Paper').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class FDPView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>FDP</span> </h3></div>"
        page = Page.objects.filter(page_name='FDP').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        charts = Charts.objects.filter(page=page)
        charts_to_show = {}
        for chart in charts:
            chart_values = []
            value = chart.values.split(',')
            j=0
            while(j<(2*chart.number_of_values)):
                chart_value = []
                chart_value.append(value[j])
                j+=1
                chart_value.append(int(value[j]))
                j+=1
                chart_values.extend([chart_value])
            charts_to_show[chart.text] = chart_values
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images, 'charts':charts_to_show})

class StudentsWorkshopView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Students' Workshop</span> </h3></div>"
        page = Page.objects.filter(page_name='Students Workshop').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class UpcomingWorkshopView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Upcoming Workshops</span> </h3></div>"
        page = Page.objects.filter(page_name='Upcoming Workshop').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class EventsView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Events</span> </h3></div>"
        page = Page.objects.filter(page_name='Events').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class ClubsView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Clubs</span> </h3></div>"
        page = Page.objects.filter(page_name='Clubs').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class ImpactStudentView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Impact On Students</span> </h3></div>"
        page = Page.objects.filter(page_name='Impact On Student').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images})

class ImpactFacultyView(View):
    template_name = 'common_page.html'

    def get(self, request, *args, **kwargs):
        display_name = "<div class='col-lg-12 mx-auto '><h3 class=' my-2'><span class='about-us'>Impact On Faculty</span> </h3></div>"
        page = Page.objects.filter(page_name='Impact On Faculty').first()
        files = Files.objects.filter(page=page)
        images = Image.objects.filter(page=page)
        charts = Charts.objects.filter(page=page)
        charts_to_show = {}
        for chart in charts:
            chart_values = []
            value = chart.values.split(',')
            j=0
            while(j<(2*chart.number_of_values)):
                chart_value = []
                chart_value.append(value[j])
                j+=1
                chart_value.append(int(value[j]))
                j+=1
                chart_values.extend([chart_value])
            charts_to_show[chart.text] = chart_values
        return render(request, self.template_name, context={'page': page, 'display_name': display_name,
                                                            'files':files, 'images':images, 'charts':charts_to_show})


class SaveContactView(View):

    def get(self, request):
        data_to_frontend = dict()
        email = request.GET['email']
        contact = request.GET['contact']
        message = request.GET['message']
        if email == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'Email cannot be empty..'
        elif contact == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'contact cannot be empty..'
        elif message == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'message cannot be empty..'
        else:
            data_to_frontend['done'] = 1
            data_to_frontend['message'] = 'Request successfully registered.'
            subject = "A registration on Human Values Website"
            message_to_show = str(email) + 'has registered'
            details = render_to_string('email_template.html', {
                'email': email,
                'contact': contact,
                'message': message,
            })
            from_mail = EMAIL_HOST_USER
            to_mail = (RECEIVER_EMAIL,)
            try:
                send_mail(subject, message_to_show, from_mail, to_mail, html_message=details, fail_silently=False)
            except:
                data_to_frontend['done'] = 0
                data_to_frontend['message'] = 'Request failed due to internal error.'
        return JsonResponse(data_to_frontend)

def view404(request):
    error_code = 404
    error_message = 'Page Not Found'
    return render(request, 'Error.html', {'error_code':error_code, 'error_message':error_message})

def view500(request):
    error_code = 500
    error_message = 'Internal Server Error'
    return render(request, 'Error.html', {'error_code':error_code, 'error_message':error_message})
