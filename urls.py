
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as clientview
from academic_performance import settings
from College_Server import views as Researchview
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', clientview.login, name="login"),
    url(r'^Register1/$', clientview.Register1, name="Register1"),
    url(r'^Add_Data_Sets/$', clientview.Add_Data_Sets, name="Add_Data_Sets"),
    url(r'^View_Student_Records/$', clientview.View_Student_Records, name="View_Student_Records"),
    url(r'^Search_Student_Data/$', clientview.Search_Student_Data, name="Search_Student_Data"),
    url(r'^ViewYourProfile/$', clientview.ViewYourProfile, name="ViewYourProfile"),
    url(r'^collegeserverlogin/$',Researchview.collegeserverlogin, name="collegeserverlogin"),
    url(r'viewallclients/$',Researchview.viewallclients,name="viewallclients"),
    url(r'^charts/(?P<chart_type>\w+)', Researchview.charts,name="charts"),
    url(r'^dislikeschart/(?P<dislike_chart>\w+)', Researchview.dislikeschart,name="dislikeschart"),
    url(r'^View_College_Dataset_Details/$', Researchview.View_College_Dataset_Details, name='View_College_Dataset_Details'),
    url(r'^Extract_PoorAcademic_PerformancePrediction/$', Researchview.Extract_PoorAcademic_PerformancePrediction, name='Extract_PoorAcademic_PerformancePrediction'),
     url(r'^Find_Student_Behavior_Prediction/$', Researchview.Find_Student_Behavior_Prediction, name="Find_Student_Behavior_Prediction"),
    url(r'^View_All_Behavioral_Change_ByLSTM/$', Researchview.View_All_Behavioral_Change_ByLSTM, name="View_All_Behavioral_Change_ByLSTM"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
