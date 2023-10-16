from django.test import SimpleTestCase
from django.urls import reverse, resolve
from frontapp.views import HomeView,ServicesView,Gallery,News,contactFormView,FooterListView,SuccessView

class TestUrls(SimpleTestCase):
    
    def test_home_url_is_resolved(self):
        url = reverse("frontapp:Home")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeView)
        
    def test_services_url_resolves(self):
        url = reverse('frontapp:Services')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,ServicesView)  
    
    def test_gallery_url_resolves(self):
        url = reverse('frontapp:Gallery')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,Gallery)  
    
    def test_news_url_resolves(self):
        url = reverse('frontapp:News')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,News)  
    
    def test_contact_form_url_resolves(self):
        url = reverse('frontapp:ContactForm')
        print(resolve(url))
        self.assertEquals(resolve(url).func,contactFormView)  
    
    def test_footer_data_url_resolves(self):
        url = reverse('frontapp:FooterData')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,FooterListView)  
    
    def test_success_urls_resolves(self):
        url = reverse('frontapp:Success')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,SuccessView)  
    
        