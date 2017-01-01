from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class Login(models.Model):
    emp_id = models.CharField(max_length=64,primary_key=True)
    emp_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255,unique=True,null=False)
    password = models.CharField(max_length=64)

    def __str__(self):
        return '%s %s %s' % (self.emp_id, self.emp_name, self.email)


class Machines(models.Model):
     EmpId = models.ForeignKey(Login,on_delete=models.CASCADE,db_column='emp_id')
     machine_id = models.CharField(max_length=255,primary_key=True)
     machine_name = models.CharField(max_length=255,unique=True,null=False)
     machine_state = models.BooleanField(default=False)
     def __str__(self):
         return '%s %s %s %s' % (self.EmpId, self.machine_id, self.machine_name, self.machine_state)




    
