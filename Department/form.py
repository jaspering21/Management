from django import forms
from Department.models import EMPLOYEE
from Department.models import DEPARTMENT

class HomeForm(forms.ModelForm):
    post = forms.CharField(required=False)

    class Meta:
        model1 = EMPLOYEE
        model2 = DEPARTMENT
        fields = ('post', )

