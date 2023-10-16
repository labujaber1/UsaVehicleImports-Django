from django.views import *
from django.test import SimpleTestCase, TestCase, Client
from  django.urls import reverse
from frontapp.models import BusinessDetails,Vehicle,Images,GeneralEnquiry,Post,Testimonials
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('frontapp:Home')
        
        
        
        
        
    def test_home_view_GET(self):
       #setup
       
       #test code
       response = self.client.get(reverse(self.home_url))
       print("test: ",self.home_url)
       print("response: ",response)
       #assertion 
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'frontapp:Home.html')