from django.db import models

# Create your models here.
class EMPLOYEE(models.Model):
    EMPLOYEE_NUM = models.CharField(max_length=15)
    EMPLOYEE_FNAME = models.CharField(max_length=15)
    EMPLOYEE_LNAME = models.CharField(max_length=15)
    DEPARTMENT_NAME = models.CharField(max_length=15)

class DEPARTMENT(models.Model):
    DEPARTMENT_NUM = models.IntegerField()
    DEPARTMENT_NAME = models.CharField(max_length=15)
    DEPARTMENT_PHONE = models.CharField(max_length=15)

