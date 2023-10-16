

from django.views import View
import requests
from django.shortcuts import render, redirect
from .models import Vehicle, Images, Post, Testimonials, BusinessDetails
from django.contrib import messages
from .forms import ContactForm
from django.views.generic import ListView

# Create your views here.

# test
# class based views to replace function based
    
    
class HomeView(ListView):
    model = Testimonials
    queryset = Testimonials.objects.all()[:3]
    context_object_name = "testimonial"
    template_name = "Home.html"


class Gallery(ListView):
    model = Images   
    context_object_name = "context"
    template_name = "Gallery.html"
    
    def get_context_data(self, **kwargs):
        context = super(Gallery, self).get_context_data(**kwargs)
        context['vehicle_images'] = Images.objects.all()
        context['vehicle'] = Vehicle.objects.all()
        return context
    
    
class News(ListView):
    model = Post
    template_name = "News.html"
    context_object_name = "context"
    
    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['data'] = BusinessDetails.objects.all()
        context['post'] = Post.objects.all()
        context['testimonial'] = Testimonials.objects.all()[3:]
        return context
    
class FooterListView(ListView):
    model = BusinessDetails
    template_name = "includes/footer.html"
    context_object_name = "context"
    
    def get_context_data(self, **kwargs):
        context = super(FooterListView, self).get_context_data(**kwargs)
        context['data'] = BusinessDetails.objects.all()
        return context

class ServicesView(View):
    def get(self,request):
        return render(request, 'Services.html')
    
class SuccessView(View):
    def get(self,request):
        return render(request, "Success.html")



# function based views
""" def home(request):
    try:
        # first 3 testimonials so the rest is in news and not repeated
        testimonial = Testimonials.objects.all()[:3]
    except Testimonials.DoesNotExist:
        raise Http404(
            "Sorry no testimonials found, I know not why but only what is!")

    return render(request, 'Home.html', {'testimonial': testimonial}) """


""" def services(request):

    return render(request, 'Services.html') """

# dynamically create each vehicle item in the db to pass and then display in a card


""" def gallery(request):
    try:
        vehicle_images = Images.objects.all()
        vehicles = Vehicle.objects.all()
    except Vehicle.DoesNotExist:
        raise Http404("Sorry vehicle not found")
    return render(request, 'Gallery.html', {'vehicle_images': vehicle_images, 'vehicle': vehicles})
 """

""" def news(request):
    try:
        post = Post.objects.all()
        data = BusinessDetails.objects.all()
        # ignore first 3 as they are displayed on home page
        testimonial = Testimonials.objects.all()[3:]
    except Post.DoesNotExist:
        raise Http404(
            "Sorry no posts or testimonials found, I know not why but only what is!")
    context = {}
    context = {'post': post, 'testimonial': testimonial, 'data': data}
    # return render(request, 'News.html', {'post': post, 'testimonial': testimonial,'data':data})
    return render(request, 'News.html', context)
 """

# display form or receive contact form data, clean fields, send as email, save to db


def contactFormView(request):
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            # sanitize form data
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data["enquiry"]
            # to use django send_mail()
            # enquiry = f"Name: {name}\nPhone Number: {phone_number}\n\n{message}"
            # prepare data to send email without adding smtp in settings
            url = "https://formspree.io/f/mbjvoewj"
            payload = {
                "name": name,
                "subject": subject,
                "email": email,
                "phone_number": phone_number,
                "message": message
            }

            try:
                response = requests.post(url, data=payload)
                print("Send mail response: ", response)
                # Raise an exception for 4xx or 5xx status codes
                response.raise_for_status()
                status_code = response.status_code
                if status_code == 200:
                    form.save()
                    messages.success(
                        request, 'A new enquiry was successfully added to the db')
                    return redirect("frontapp:Success")
                else:
                    messages.error(
                        request, 'An error occurred while sending the email')
            except requests.RequestException as e:
                print("An error occurred while sending the email:", e)
                messages.error(
                    request, 'An error occurred while sending the email')
        else:
            messages.error(request, 'An error occurred saving a new enquiry')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'ContactForm.html', context)


""" def successView(request):

    return render(request, "Success.html") """


""" def footerData(request):
    try:
        data = BusinessDetails.objects.all()
    except BusinessDetails.DoesNotExist:
        raise Http404(
            "Sorry no business data found, I know not why but only what is!")
    context = {}
    context = {'data': data}

    return render(request, 'Footer.html', context) """

