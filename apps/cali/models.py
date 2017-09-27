# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re 
from datetime import date, datetime
from django.utils import timezone

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z ]+$')
# PHONE_REGEX = re.compile(r'^\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}+$')

# Create your models here.


class Menu(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.CharField(max_length=10)
    # auto_now_add=True - adds the current date/time when object is created.
    created_at = models.DateTimeField(auto_now_add = True)
    # auto_now=True - automatically updates anytime the object is modified
    updated_at = models.DateTimeField(auto_now = True)
    # objects=menuManager()

    # build string representation of the object
    def __str__(self):
        return self.category + ' - ' + self.title + ' - ' + self.description + ' - ' + self.price



class ReservationManager(models.Manager):
    def add(self, data):
        errors = []

        #validating first and last name
        if len(data['first_name']) < 2:
            errors.append('First name must be at least two characters long')
        if not data['first_name'].isalpha():
            errors.append('First name may only be letters')
        if len(data['last_name']) < 2:
            errors.append('Last name must be at least two characters long')
        if not data['last_name'].isalpha():
            errors.append('Last name may only be letters')

        #validating phone number
        if len(data['phone_number']) < 10:
            errors.append('Phone number must be 10 digits long.')
        if not data['phone_number'].isdigit():
            errors.append('Phone must be only in numbers')
        
        #validating email
        if data['email_address'] == '':
            errors.append('Email cannot be blank')
        if not EMAIL_REGEX.match(data['email_address']):
            errors.append('Please enter valid email address')
        
        #Validating email uniqueness
        # try:
        #     Reservation.objects.get(email_address=data['email_address'])
        #     errors.append(email_three='Email is already registered')
        # except:
        #     pass

        #validating number of guests
        if data['number_guests'] < 12:
            errors.append('Must be minimum of 12 guests')
        if not data['number_guests'].isdigit():
            errors.append('Guest# must be only in numbers')

        #validating date
        if data['date']:
            if str(data['date']) < str(date.today()):
                errors.append('Date cannot be set in the past')
            if data['date'] == '':
                errors.append('Date cannot be empty')

        #validating time
        # if data['time']:
        #     if str(data['time']) < str(datetime.now().time()):
        #         errors.append('Time cannot be set in the past')
            if data['time'] == '':
                errors.append('Time cannot be empty')

        #validating date and time availability
        if data['date'] == '':
            pass
        
        else:
            if len(Reservation.objects.filter(date = data['date'], time = data['time'])) > 0:
                errors.append('Not available date/time, please choose different time and/or date')
        

        # after validations - returning results
        if len(errors) == 0:
            new_table = Reservation.objects.create(first_name=data['first_name'], last_name=data['last_name'], phone_number=data['phone_number'], email_address=data['email_address'], number_of_guests=data['number_guests'],date=data['date'], time=data['time'], message=data['request_msg'] )

            return {
                'new': new_table,
                'error_list': None
            }
        else:
            print(errors)
            return {
                'new': None,
                'error_list': errors
            }



class Reservation(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    email_address = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ReservationManager()

    # build string representation of the object
    def __str__(self):
        return self.first_name + ' - ' + self.last_name + ' - ' + self.phone_number + ' - ' + self.email_adress + ' - ' + self.number_of_guests + ' - ' + self.date + ' - ' + self.time + ' - ' + self.message