from django.urls import path  
from screens import views as screen 
urlpatterns = [  
    path('doctor', screen.doctorLogin, name="doctorLogin"),
    path('doctor/dashboard',screen.doctorDash, name="doctorDash"),  
    path('user', screen.staffLogin, name="staffLogin"),
    path('user/createStaff', screen.createStaff, name="createStaff"),
    path('user/createDoctor', screen.createDoctor, name="createDoctor"),  
    path('user/createAppointment', screen.createApp, name="createApp"),
    path('user/dashboard', screen.staffDash, name="staffDash"),  
    path('logout',screen.logout,name="logout"),
    path('logoutStaff',screen.logoutStaff, name="logoutStaff"),
    path('break',screen.takeBreak, name="takeBreak"),
    path('delete/<int:id>/',screen.deleteApp,name="deleteApp"),
    path('emergency/<int:id>/',screen.emergencyApp,name="emergencyApp"),
    path('',screen.home, name="home"),
]  