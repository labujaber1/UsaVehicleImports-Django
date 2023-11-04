
from django.urls import reverse, reverse_lazy


import requests
from django.shortcuts import get_object_or_404, render, redirect
from .models import PreviousExamplesImages,Faqs,Vehicle, Comment, Images, Post, Testimonials, BusinessDetails
from django.contrib import messages
from .forms import ContactForm, CommentForm, LikeForm
from django.views.generic import ListView,View

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
        context['peImages'] = PreviousExamplesImages.objects.all()
        return context
    
    
class News(ListView):
    model = Comment
    template_name = "News.html"
    context_object_name = "context"
    
    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)
        context['data'] = BusinessDetails.objects.all()      
        context['post'] = Post.objects.all()
        context['testimonial'] = Testimonials.objects.all()[3:]
        context['comment_form'] = CommentForm()
        return context
    
    def post(self,request,id):
        post_obj = get_object_or_404(Post,id=id)
        # check if already liked using session log
        if str(id) in request.session.get('liked_posts', []):
            warning_message = f"You have already liked the {post_obj.title} post."
            messages.warning(request, warning_message)
            return redirect('/News/#'+str(id),{'post_obj': post_obj})
        post_obj.likes += 1
        # Assign current post to comment
        try:
            # Save comment to db
            post_obj.save()
            request.session.setdefault('liked_posts', []).append(str(id))
            request.session.modified = True
            success_message = f"A like was given to the post {post_obj.title}."
            messages.success(request, success_message)
            return redirect('/News/#'+str(id),{'post_obj': post_obj})
        except Exception as e:
            messages.error(request, "Apologies but an error occurred liking the post. Please try again.") 
            messages.error(request, str(e))
        
        context = {'post_obj': post_obj}
        return redirect('/News/#'+str(id) , context )   
        
    
class FooterListView(ListView):
    model = BusinessDetails
    template_name = "includes/footer.html"
    context_object_name = "context"
    
    def get_context_data(self, **kwargs):
        context = super(FooterListView, self).get_context_data(**kwargs)
        context['data'] = BusinessDetails.objects.all()
        return context

class ServicesView(ListView):
    model = Faqs
    template_name = "Services.html"
    context_object_name = "context"
    
    def get_context_data(self,**kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['faqs'] = Faqs.objects.all()      
        #context['services-content'] = ServicesContent.objects.all()
        return context
    
class SuccessView(View):
    def get(self,request):
        return render(request, "Success.html")


#django central
class CommentOnPostView(ListView):
    
    def get(self, request,id):
        post_obj = get_object_or_404(Post,id=id)
        comment_form = CommentForm()
        context = {'comment_form':comment_form,'post_obj':post_obj}
        return render(request, 'includes/commentsForm.html', context)
    
    def post(self,request,id):
        post_obj = get_object_or_404(Post,id=id)
        new_comment = None   
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            #comment_form = comment_form.cleaned_data
            # Create Comment object, don't save to db
            new_comment = comment_form.save(commit=False)
            # Assign current post to comment
            new_comment.post = post_obj
            try:
                # Save comment to db
                new_comment.save()
                success_message = f"A new comment was successfully submitted for post {post_obj.title} and awaiting moderation."
                messages.success(request, success_message)
                return redirect('/News/#'+str(id))
            except Exception as e:
                messages.error(request, "Apologies but an error occurred submitting your comment. Please try again.") 
                messages.error(request, str(e))
        
        # if not valid return to form      
        comment_form = CommentForm()
        context = {'post_obj': post_obj,'new_comment': new_comment,'comment_form': comment_form}
        
        return redirect('/News/#'+str(id) , context )   
    
    
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


                                           
                                           
                                           

