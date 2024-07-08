from django.db import models  
class Doctor(models.Model):  

    name = models.CharField(max_length=100,default="")
    contact = models.CharField(max_length=10,default="") 
    pwd = models.CharField(max_length=20,default="")
    status = models.CharField(max_length=11,default="unavailable")
    count = models.IntegerField(default=0,max_length=3)
    checkedIn = models.CharField(default="F",max_length=1)
    class Meta:  
        db_table = "doctors" 
