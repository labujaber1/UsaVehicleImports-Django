

from django.http import Http404
from django.urls import reverse
from django.views import View
import requests
from django.shortcuts import get_object_or_404, render, redirect
from .models import Vehicle, Comment, Images, Post, Testimonials, BusinessDetails
from django.contrib import messages
from .forms import ContactForm,CommentForm,LikeForm
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
    model = Comment
    template_name = "News.html"
    context_object_name = "context"
    
    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['data'] = BusinessDetails.objects.all()
        queryset = Post.objects.all()
        #queryset = queryset.filter(comments__active=False)
        context['post'] = queryset
        context['testimonial'] = Testimonials.objects.all()[3:]
        context['comment_form'] = CommentForm()
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


#djangocentral
class PostDetailView(View):
    template_name = 'includes/commentsForm.html'
    
    def get(self, request,id):
        post = get_object_or_404(Post,id=id)
        comment_form = CommentForm()
        context = {'comment_form':comment_form,'post':post}
        return render(request, 'News.html', context)
    
    def post(self,request,id):
        post = get_object_or_404(Post,id=id)
        #comments = post.comments.filter(active=False)
        new_comment = None    # Comment posted
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            # Create Comment object, don't save to db
            new_comment = comment_form.save(commit=False)
            # Assign current post to comment
            new_comment.post = post
            # Save comment to db
            new_comment.save()
            messages.success(
                        request, 'A new comment was successfully made by a user')
            return redirect('/News/')
          
        else:
            comment_form = CommentForm()
        context = {'post': post,'new_comment': new_comment,'comment_form': comment_form}
        return render(request, self.template_name, context )   
    
    
# function based views
# display form or receive contact form data, clean fields, send as email, save to db

#serializers

    
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


                                           
                                           
                                           

