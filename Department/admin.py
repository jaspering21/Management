from django.contrib import admin
from .models import EMPLOYEE
from .models import DEPARTMENT

# Register your models here.
admin.site.register(EMPLOYEE)
admin.site.register(DEPARTMENT)

