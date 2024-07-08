from django.db import models  
class Staff(models.Model):  

    name = models.CharField(max_length=100,default="")
    contact = models.CharField(max_length=10,default="") 
    pwd = models.CharField(max_length=20,default="")
    class Meta:  
        db_table = "staffs" 

