from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponse
import time
from django.db import transaction
from appointments.models import Appointment
from doctor.models import Doctor

def my_periodic_task():
    assign_doctor_to_appointments()

scheduler = BackgroundScheduler()
scheduler.add_job(my_periodic_task, 'interval', seconds=5)

def start_scheduler():
    scheduler.start()

def stop_scheduler():
    scheduler.shutdown()

def assign_doctor_to_appointments():
    # Get appointments with no assigned doctor or a doctor with status 'u' or 'b'
    appointments_without_doctor = Appointment.objects.filter(doctor_name='')
    '''unavailable_or_busy_doctor = Doctor.objects.filter(status = ['unavailable','break'])
    appointments_with_unavailable_or_busy_doctor = Appointment.objects.filter(doctor_name=unavailable_or_busy_doctor.name)

    appointments_to_assign = appointments_without_doctor.union(appointments_with_unavailable_or_busy_doctor)'''
    appointments_to_assign = appointments_without_doctor
    '''
    # Iterate over appointments with preferences
    for appointment in appointments_to_assign.filter(preferred_doctor=''):
        preferred_doctor = appointment.preferred_doctor

        # Check if the preferred doctor is available
        if (
            preferred_doctor.status == 'a'
            and preferred_doctor.checkedIn == 't'
            and preferred_doctor.count < some_limit
        ):
            with transaction.atomic():
                # Assign the preferred doctor to the appointment
                appointment.doctor = preferred_doctor
                appointment.save()

                # Update the count for the assigned doctor
                preferred_doctor.count += 1
                preferred_doctor.save()'''

    for appointment in appointments_to_assign:
        # Get an available doctor with the least count for appointments without preferences
        available_doctor = Doctor.objects.filter(status='available', checkedIn='T').order_by('count').first()
        print('doctor:',available_doctor)
        if available_doctor:
            with transaction.atomic():
                # Assign the available doctor to the remaining appointments without preferences
                appointment.doctor_name = available_doctor.name
                # Update the count for the assigned doctor
                available_doctor.count += 1
                available_doctor.save()
                appointment.save()