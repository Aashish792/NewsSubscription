from django.shortcuts import render,redirect
from .models import Subscription
from .forms import SubscriptionForm

from django.contrib.sites.shortcuts import get_current_site
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request,'home.html')


def SubscriptionView(request):
    form = SubscriptionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST.get('subscription_emails')
            # to check if email exist or not
            if Subscription.objects.filter(subscription_emails=email).exists():
                send_mail(
                    'Email Verify',
                    f'You are already our member!',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return HttpResponse('The Email has been sent')
            else:
                user = form.save(commit=False)
                # http://<Domain_name>.com/verify/<token>
                domain_name = get_current_site(request).domain
                token = str(random.random()).split('.')[1]
                user.token = token
                user.save()
                print(user)

                link = f'http://{domain_name}/verify/{token}'

                send_mail(
                    'Email Verify',
                    f'Please click {link} to verify your email',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return HttpResponse('The Email has been sent')


    return render(request,'register.html',{'form':form})

def verify(request,token):
    try:
        user = Subscription.objects.get(token=token)
        print(user,"varify Token")
        user.is_verified = True
        user.save()
        return redirect('http://google.com/')
    except Exception as e:
        msg = e
        return render(request, 'final.html', {'msg':msg})
