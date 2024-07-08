from django.shortcuts import render,redirect
from staff.forms import StaffForm
from doctor.forms import DoctorForm
from appointments.forms import AppointmentForm
from django.contrib import messages
from staff.models import Staff
from doctor.models import Doctor
from appointments.models import Appointment
from datetime import date
from twilio.rest import Client
from django.db.models import F
from SmartClinic.scheduler import start_scheduler,stop_scheduler

def home(request):
    return render(request, 'screens/home.html')

def createStaff(request):  
    if request.method == "POST":  
        form = StaffForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                messages.success(request,f'User Created') 
                return redirect('/user')  
            except:  
                pass  
    else:  
        form = StaffForm()  
    return render(request,'screens/createStaff.html',{'form':form})

def staffLogin(request):
    if request.method == "POST":  
        form = StaffForm(request.POST)
        try:
            staff = Staff.objects.get(contact=form['contact'].data)
            if staff.pwd==form['pwd'].data :
                request.session['staffID'] = staff.contact
                start_scheduler()
                return redirect('/user/dashboard')
            else :
                messages.success(request,f'Password Incorrect')
                return redirect('/user')
        except:
            messages.success(request,f'User Not Found!')
            return redirect('/user')
    else:  
        form = StaffForm()   
    return render(request, 'screens/staffLogin.html',{'form': form})

def staffDash(request):  
    if(request.session['staffID']):
        staffID = request.session.get('staffID')
        staff = Staff.objects.get(contact=staffID)
        appointments = Appointment.objects.filter(date=date.today())
        return render(request,"screens/staffDashboard.html",{'staff':staff,'appointments':appointments})
    else:
        return redirect('/user')

def createDoctor(request): 
    if(request.session['staffID']):
        if request.method == "POST":  
            form = DoctorForm(request.POST)  
            print(request.session['staffID'])
            if form.is_valid():  
                try:  
                    form.save() 
                    messages.success(request,f'Doctor Created') 
                    return redirect('/user/dashboard')  
                except:  
                    pass  
        else:  
            form = DoctorForm()  
        return render(request,'screens/createDoctor.html',{'form':form})
    else:
        return redirect('/user') 

def createApp(request):
    if(request.session['staffID']):
        if request.method == "POST":  
            form = AppointmentForm(request.POST)  
            if form.is_valid():  
                try:  
                    my_model_instance = form.save(commit=False)
                    my_model_instance.date = date.today()
                    '''scheduled_doctor_name = get_consulting_doctor()
                    my_model_instance.doctor_name = scheduled_doctor_name'''
                    my_model_instance.save()
                    messages.success(request,f'Appointment Created') 
                    return redirect('/user/dashboard')  
                except:  
                    pass  
        else:  
            form = AppointmentForm()
        return render(request,'screens/makeAppointment.html',{'form':form})
    else:
        return redirect('/user')

def doctorLogin(request):
    if request.method == "POST":  
        form = DoctorForm(request.POST)
        try:
            doctor = Doctor.objects.get(contact=form['contact'].data)
            if doctor.pwd==form['pwd'].data :
                request.session['doctorID'] = doctor.contact
                doctor.status = 'available'
                doctor.checkedIn = 'T'
                doctor.save()
                return redirect('/doctor/dashboard')
            else :
                messages.success(request,f'Password Incorrect')
                return redirect('/doctor')
        except:
            messages.success(request,f'Admin Not Found! Contact Helpdesk')
            return redirect('/doctor')
    else:  
        form = DoctorForm()   
    return render(request, 'screens/doctorLogin.html',{'form': form})

def doctorDash(request):  
    if(request.session['doctorID']):
        doctorID = request.session.get('doctorID')
        doctor = Doctor.objects.get(contact=doctorID)
        appointments = Appointment.objects.filter(date=date.today(),doctor_name=doctor.name)
        return render(request,"screens/doctorDashboard.html",{'doctor':doctor,'appointments':appointments})
    else:
        return redirect('/doctor')  

def deleteApp(request, id):  
    appointment = Appointment.objects.get(id=id) 
    doctor = Doctor.objects.get(name=appointment.doctor_name)
    count = doctor.count
    doctor.count = count - 1
    doctor.save()
    appointment.delete()
    return redirect('/doctor/dashboard')

def takeBreak(request):
    activeID = request.session.get('doctorID')
    if(activeID):
        doctor = Doctor.objects.get(contact=activeID)
        doctor.status = 'break'
        doctor.count = 0
        doctor.save()
        del request.session['doctorID']
        '''appointments = Appointment.objects.filter(doctor_name=doctor.name)
        appointment_ids = appointments.values_list('id', flat=True)
        rescheduleApp(list(appointment_ids))'''
    return redirect('/')

def emergencyApp(request, id):
    account_sid = 'account_sid'
    auth_token = 'auth_token'
    twilio_number = '+twilio_number'
    my_phone_number = '+my_phone_number'
    client = Client(account_sid, auth_token)
    appointment = Appointment.objects.get(id=id) 
    messageBody = "Emergency Appointment:"+"\nID: "+str(appointment.id)+"\nName: "+appointment.name+"\nAge: "+appointment.age
    message = client.messages.create(body=messageBody,from_=twilio_number,to=my_phone_number)
    doctor = Doctor.objects.get(name=appointment.doctor_name)
    count = doctor.count
    doctor.count = count - 1
    doctor.save()
    appointment.delete()
    return redirect('/user/dashboard')

def logout(request):
    activeID = request.session.get('doctorID')
    if(activeID):
        doctor = Doctor.objects.get(contact=activeID)
        doctor.status = 'unavailable'
        doctor.count = 0
        doctor.save()
        del request.session['doctorID']
    return redirect('/')

def logoutStaff(request):
    activeID = request.session.get('staffID')
    if(activeID):
        stop_scheduler()
        del request.session['staffID']
    return redirect('/')


