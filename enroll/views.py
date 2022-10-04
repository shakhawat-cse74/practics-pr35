from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validated')
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Pass:', fm.cleaned_data['password'])
    else:
        fm = StudentRegistration()
    return render (request,'enroll/registrationform.html', {'form':fm})