from django.db import models  

class Appointment(models.Model):  
  
    name = models.CharField(max_length=100,default="")
    contact = models.CharField(max_length=10,default="") 
    age = models.CharField(max_length=2,default="")
    date = models.DateField(max_length=10,default="")
    preference = models.BigIntegerField(default='',choices=(("1","A"),("2","B"),("3","C"),))
    doctor_id = models.ForeignKey(default='',on_delete=models.SET_NULL, null=True, to='doctor.Doctor')
    
    class Meta:  
        db_table = "appointments" 

