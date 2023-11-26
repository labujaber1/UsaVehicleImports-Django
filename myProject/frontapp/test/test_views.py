from django.views import *
from django.test import SimpleTestCase, TestCase, Client
from  django.urls import reverse
from frontapp.models import BusinessDetails,Vehicle,Images,GeneralEnquiry,Post,Testimonials
import json

class TestViews(TestCase):
    