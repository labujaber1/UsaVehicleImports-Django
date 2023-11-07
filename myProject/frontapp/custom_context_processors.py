
from .models import NavHTMLPage,BusinessDetails
from .forms import ContactForm
import requests
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ContactForm

def get_business_data(request):
    data = BusinessDetails.objects.all()
    navLink = NavHTMLPage.objects.all()
    context = {'data': data,'navLink':navLink}
    return context

def get_form_data(request):
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
    return ( context)