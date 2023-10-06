
import requests
from django.shortcuts import render, redirect
from .models import Vehicle, Images, Post, GeneralEnquiry, Testimonials, BusinessDetails
from django.http import HttpResponse
from django.http import Http404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import ContactForm
from icecream import ic

# Create your views here.

# test


def home(request):
    try:
        # first 3 testimonials so the rest is in news and not repeated
        testimonial = Testimonials.objects.all()[:3]
    except Testimonials.DoesNotExist:
        raise Http404(
            "Sorry no testimonials found, I know not why but only what is!")

    return render(request, 'Home.html', {'testimonial': testimonial})


def services(request):

    return render(request, 'Services.html')

# dynamically create each vehicle item in the db to pass and then display in a card


def gallery(request):
    try:
        vehicle_images = Images.objects.all()
        vehicles = Vehicle.objects.all()
    except Vehicle.DoesNotExist:
        raise Http404("Sorry vehicle not found")
    return render(request, 'Gallery.html', {'vehicle_images': vehicle_images, 'vehicle': vehicles})


def news(request):
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


# display form or receive contact form data, clean fields, send as email, save to db


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            # sanitize form data
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data["enquiry"]
            # to use django send_mail()
            # enquiry = f"Name: {name}\nPhone Number: {phone_number}\n\n{message}"
            # prepare data to send email without adding smtp in settings
            url = "https://formspree.io/f/mbjvoewj"
            payload = {
                "name": name,
                "subject": subject,
                "from_email": from_email,
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
                    return redirect("Success")
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


def successView(request):

    return render(request, "Success.html")


def footerData(request):
    try:
        data = BusinessDetails.objects.all()
    except BusinessDetails.DoesNotExist:
        raise Http404(
            "Sorry no business data found, I know not why but only what is!")
    context = {}
    context = {'data': data}

    return render(request, 'Footer.html', context)
