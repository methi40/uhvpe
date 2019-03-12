from django.conf.urls import url
from .views import (IndexView, DirectorMessageView, VisionAndMissionView, EstablishmentView, StructureView, SyllabusView,
                    SyllabusView, BookAndAuthorsView, UnitWiseNotesView, VideoLecturesView, UnitWisePPTView, UTQuestionPaperView, 
                    PreviousPaperView, FDPView, StudentsWorkshopView, UpcomingWorkshopView, EventsView, ClubsView,
                    ImapactStudentView, ImapactFacultyView, SaveContactView)
                    

urlpatterns = [
    url(r'^director-message/$', DirectorMessageView.as_view(), name='director-message'),
    url(r'^vision-and-mission/$', VisionAndMissionView.as_view(), name='vision-and-mission'),
    url(r'^establishment/$', EstablishmentView.as_view(), name='establishment'),
    url(r'^structure/$', StructureView.as_view(), name='structure'),
    url(r'^syllabus/$', SyllabusView.as_view(), name='syllabus'),
    url(r'^book-and-authors/$', BookAndAuthorsView.as_view(), name='book-and-authors'),
    url(r'^unit-wise-notes/$', UnitWiseNotesView.as_view(), name='unit-wise-notes'),
    url(r'^video-lectures/$', VideoLecturesView.as_view(), name='video-lectures'),
    url(r'^unit-wise-ppt/$', UnitWisePPTView.as_view(), name='unit-wise-ppt'),
    url(r'^UT-question-paper/$', UTQuestionPaperView.as_view(), name='UT-question-paper'),
    url(r'^previous-paper/$', PreviousPaperView.as_view(), name='previous-paper'),
    url(r'^fdps/$', FDPView.as_view(), name='fdps'),
    url(r'^students-workshop/$', StudentsWorkshopView.as_view(), name='students-workshop'),
    url(r'^upcoming-workshop/$', UpcomingWorkshopView.as_view(), name='upcoming-workshop'),
    url(r'^events/$', EventsView.as_view(), name='events'),
    url(r'^clubs/$', ClubsView.as_view(), name='clubs'),
    url(r'^imapact-student/$', ImapactStudentView.as_view(), name='imapact-student'),
    url(r'^imapact-faculty/$', ImapactFacultyView.as_view(), name='imapact-faculty'),
    url(r'^savecontact$', SaveContactView.as_view(), name='save_contact'),
    url(r'^$', IndexView.as_view(), name='home'),
]
