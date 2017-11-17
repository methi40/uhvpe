from django.conf.urls import url
from .views import IndexView, DirectorMessageView, UHVPESyllabus, GuidelineView, SociallyRelevantProjectView, \
    BookView, FAQView, JourneySoFarView, ImpactView, FuturePlansView, NodalCenterView

urlpatterns = [
    url(r'^directormessage/$', DirectorMessageView.as_view(), name='director-message'),
    url(r'^syllabus/$', UHVPESyllabus.as_view(), name='syllabus'),
    url(r'^guidelines/$', GuidelineView.as_view(), name='guidelines'),
    url(r'^projects/$', SociallyRelevantProjectView.as_view(), name='projects'),
    url(r'^books/$', BookView.as_view(), name='books'),
    url(r'^faq/$', FAQView.as_view(), name='faq'),
    url(r'^journey/$', JourneySoFarView.as_view(), name='journey'),
    url(r'^impact/$', ImpactView.as_view(), name='impact'),
    url(r'^futureplans/$', FuturePlansView.as_view(), name='future'),
    url(r'^nodalcenter/$', NodalCenterView.as_view(), name='nodal-center'),
    url(r'^$', IndexView.as_view(), name='home'),
]
