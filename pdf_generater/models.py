# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# gender selection options
FEMALE = 1
MALE = 2
GENDER_CHOICES = (
    (FEMALE, 'Female'),
    (MALE, 'Male'),
)


class PatientDetails(models.Model):

	prefix = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)
	date_of_birth = models.DateField(blank=True, null=True)
	age = models.SmallIntegerField(blank=True, default=18)
	home_address = models.CharField(blank=True, max_length=200)
	address = models.CharField(blank=True, max_length=100)
	city = models.CharField(blank=True, max_length=100)
	state = models.CharField(blank=True, max_length=100)
	zip_code = models.IntegerField(blank=True)
	country = models.CharField(blank=True, max_length=100)

	gender = models.SmallIntegerField(
        choices=GENDER_CHOICES,
        default=FEMALE,
    )

    home_phone_number = models.IntegerField(blank=True)
    mobile_number = models.IntegerField(blank=True)
    email = models.CharField(max_length=50, blank=True)
    medicare_number = models.CharField(max_length=50, blank=True)
    ethinicity = models.CharField(max_length=50, blank=True)


class ProviderDetails(models.Model):

	prefix = models.CharField(max_length=10)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)
	date_of_birth = models.DateField(blank=True, null=True)
	age = models.SmallIntegerField(blank=True, default=18)
	home_address = models.CharField(blank=True, max_length=200)