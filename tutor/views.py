import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from .forms import ReviewForm, CallBackForm
from .models import Review, CallBack



# Create your views here.


def index_view(request):
    context = {
    }
    return render(request, "home.html", context)


#######################################################
# REVIEWS
#######################################################
def reviews_view(request):
    reviews = Review.objects.all()
    reviews_ser = serializers.serialize('json', reviews)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
        
    context = {
        'reviews_ser' : reviews_ser,
        'form': form,
    }
    return render(request, 'reviews.html', context)


#######################################################


#######################################################
# CallBack
#######################################################

def callback_view(request):
    callback = CallBack.objects.all()
    if request.method == 'POST':
        form = CallBackForm(request.POST)
        if form.is_valid():
            #email = form.cleaned_data['email']
            #number = form.cleaned_data['number']
            #message = form.cleaned_data['message']
            email = request.POST['email']
            number = request.POST['number']
            message = request.POST['message']
            form.save()
            send_mail("Request Callback", f"Callback request from : {email}, {number},\n\n{message}", "mansimran2001@googlemail.com", ["mansimran2001@googlemail.com"])
            send_mail("Thank you for reaching out!", f"Dear Parent,\n\nThank you for requesting a callback. We have received your request and will get in touch with you as soon as possible on {number}.\n\nBest regards\n", "mansimran2001@googlemail.com", [f"{email}"])
            return redirect('callbacks')
        else:
            return HttpResponse(form.errors)
    else:
        form = CallBackForm()
    context = {
        'form': form,
    }
    return render(request, 'callback.html', context)


#######################################################


def contactus_view(request):
    return render(request, 'contact-us.html')


def about_view(request):
    return render(request, 'aboutus.html')


def navbar(request):
    return render(request, 'navbar.html')

def maths_view(request):
    return render(request, 'maths.html')

def physics_view(request):
    return render(request, 'physics.html')

def test_view(request):
    callback = CallBack.objects.all()
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('test')

    context = {
        'form': form,
    }
    return render(request, 'test.html', context)