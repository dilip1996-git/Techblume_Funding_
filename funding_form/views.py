from django.shortcuts import render,redirect
from .models import Application
from .forms import ApplicationForm


def submit_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'funding_form/thankyou.html')
    else:
        form = ApplicationForm()
    
    return render(request, 'funding_form/form.html', {'form': form})

# Create your views here.
