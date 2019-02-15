from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from Department.models import EMPLOYEE
from Department.models import DEPARTMENT
from Department.form import HomeForm

def homepage(request):
    teplate_name = 'Homepage.html'
    return render(request, 'Homepage.html')

    '''def get(self, request):
        #posts = EMPLOYEE.objects.all()
        #form = HomeForm()
        #args = {'form': form, 'posts': posts}
        #return render(request, 'Homepage.html')'''


    '''def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('hpme:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)'''

