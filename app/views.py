from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'index.html')



def Messageform(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            msg = form.cleaned_data.get('message')
            sub = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')

            # send_mail(subject, message, settings.EMAIL_HOST_USER, ['vu3tpz@gmail.com'], fail_silently=False)
            send_mail(sub,f'Name:{name}\nEmail id:{email}\nMessage:{msg}', settings.EMAIL_HOST_USER , ['cerenbusinessindia@gmail.com'],fail_silently=False)
            #change to cerenbusinessindia@gmail.com
            form = EmailForm()
            return redirect('/')
        form=EmailForm()
    return render(request, 'index.html', {'form': form})