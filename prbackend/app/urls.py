from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.LoginAPIView, name='LoginAPIView'),
    path('getData/',views.getData, name='getData'),
    path('postData/',views.postData, name='postData'),

    path('LoginAPIView/',views.LoginAPIView, name='LoginAPIView'),
    path('Listprojects/', views.Listprojects, name='Listprojects'),
    path('Listemployees/', views.Listemployees, name='Listemployees'),
    path('AddprojectData/', views.AddprojectData, name='AddprojectData'),
    path('AddemployeeData/', views.AddemployeeData, name='AddemployeeData'),
    path('deleteproject/<int:projectId>',views.deleteproject, name='deleteproject'),
    path('projectdetailview/<int:projectId>', views.projectdetailview, name='projectdetailview'),
    path('assignedemployeedata/<int:projectId>', views.assignedemployeedata, name='assignedemployeedata'),
    path('Assignproject_team/',views.Assignproject_team, name='Assignproject_team'),
    path('Listemployees_projectassign/<int:projectId>', views.Listemployees_projectassign, name='Listemployees_projectassign'),
    path('deleteuser/<int:userID>', views.deleteuser, name='deleteuser'),
    path('getemployee_updates/<int:id>', views.getemployee_updates, name='getemployee_updates'),
    path('UpdateUser/<int:id>', views.UpdateUser, name='UpdateUser'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)