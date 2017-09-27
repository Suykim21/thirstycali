# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import Menu, Reservation

# def index(request):
#     print ("*" *50)
#     return render(request, 'cali/index.html')

def home(request):
    print ("*" *50)
    return render(request, 'cali/home.html')

def menu(request):
    print ("*" *50)
    starters = Menu.objects.filter(category="starters").all()
    burgers = Menu.objects.filter(category="burgers").all()
    belgian = Menu.objects.filter(category="belgian").all()
    german = Menu.objects.filter(category="german").all()
    non_alcoholic = Menu.objects.filter(category="non_alcoholic").all()
    return render(request, 'cali/menu.html', { 'starters': starters, 'burgers': burgers, 'belgians': belgian, 'germans': german, 'non_alcoholics': non_alcoholic})

def reservation(request):
    print ("*" *50)
    return render(request, 'cali/reservation.html')

def addreservation(request):
    print ("*" * 50)
    context = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'phone_number': request.POST['phone_number'],
        'email_address': request.POST['email_address'],
        'number_guests': request.POST['number_guests'],
        'date': request.POST['date'],
        'time': request.POST['time'],
        'request_msg': request.POST['request_msg'],
    }

    add_result = Reservation.objects.add(context)

    if add_result['new'] != None:
        messages.success(request, 'Successfully Booked, Cheers!')
        return redirect('/reservation')
    else:
        for error_str in add_result['error_list']:
            messages.error(request, error_str)
        return redirect('/reservation')