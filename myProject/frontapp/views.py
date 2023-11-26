
import requests
from django.shortcuts import get_object_or_404, render, redirect
from .models import NavHTMLPage,EditableStaticContent,PreviousExamplesImages,Faqs,Vehicle, Comment, Images, Post, Testimonials, BusinessDetails
from django.contrib import messages
from .forms import ContactForm, CommentForm
from django.views.generic import ListView,View
from datetime import datetime

def get_object_or_custom_404(model,id):
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        return redirect("frontapp:Error404")
  
# class based views to replace function based  
class HomeView(ListView):
    model = Testimonials
    context_object_name = "testimonial"
    template_name = "Home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            context['testimonial'] = Testimonials.objects.all()[:3]
        except Testimonials.DoesNotExist:
            context['testimonial'] = None
        context['editableStaticContent'] = EditableStaticContent.objects.all()
        context['navHTMLPage'] = NavHTMLPage.objects.all()
        
        return context


class Gallery(ListView):
    model = Images   
    context_object_name = "context"
    template_name = "Gallery.html"
    
    def get_context_data(self, **kwargs):
        context = super(Gallery, self).get_context_data(**kwargs)
        context['vehicle_images'] = Images.objects.all()
        context['vehicle'] = Vehicle.objects.all()
        context['peImages'] = PreviousExamplesImages.objects.all()
        context['editableStaticContent'] = EditableStaticContent.objects.all()
        
        return context


    
class News(ListView):
    model = Comment
    template_name = "News.html"
    context_object_name = "context"
    
    def get_context_data(self, **kwargs):
        context = super(News, self).get_context_data(**kwargs)     
        context['post'] = Post.objects.all()
        context['testimonial'] = Testimonials.objects.all()[3:]
        context['editableStaticContent'] = EditableStaticContent.objects.all()
        context['comment_form'] = CommentForm()
        return context
    
    def post(self,request,id): 
        post_obj = get_object_or_custom_404(Post,id=id)
     
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
        context['editableStaticContent'] = EditableStaticContent.objects.all()
              
        return context
    
class SuccessView(View):
    def get(self,request):
        return render(request, "Success.html")

class Error404View(View):
    def get(self,request):
        return render(request, "Error404.html")
    
#django central
class CommentOnPostView(ListView):
    
    def get(self, request,id):
        post_obj = get_object_or_custom_404(Post,id=id)
        comment_form = CommentForm()
        context = {'comment_form':comment_form,'post_obj':post_obj}
        return render(request, 'includes/commentsForm.html', context)
    
    def post(self,request,id):
        post_obj = get_object_or_custom_404(Post,id=id)
        new_comment = None   
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
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
    
    
# function based views ########

# pass in form and clean data 
def validate_contact_form(form):
    name = form.cleaned_data["name"]
    subject = form.cleaned_data["subject"]
    email = form.cleaned_data["email"]
    phone_number = form.cleaned_data["phone_number"]
    message = form.cleaned_data["enquiry"]
    last_name = form.cleaned_data["last_name"]
    #honeypot check for bots, hidden from user in html page
    if last_name is not None:
        return False
    else:
        return name, subject, email, phone_number, message, last_name
    
# pass in cleaned form data and send in an email
def send_email(name, subject, email, phone_number, message, last_name):
    url = "https://formspree.io/f/mbjvoewj"
    payload = {
        "name": name,
        "subject": subject,
        "email": email,
        "phone_number": phone_number,
        "message": message,
        "last_name":last_name
    }
    try:
        response = requests.post(url, data=payload)
        print("Send mail response: ", response)
        response.raise_for_status()
        status_code = response.status_code
    except requests.RequestException as e:
            print("An error occurred within the send_email() function. Error: ", e)
            messages.error(
                'Error code: ',e)
    
    return status_code
    
# process contact form and return result
def processContactFormView(request):
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST or None)
        
        if form.is_valid():
            date = datetime.now()
            #return boolean
            clean_form = validate_contact_form(form)
            if clean_form is not False:
                name, subject, email, phone_number, message, last_name = clean_form
                status_code = send_email(name, subject, email, phone_number, message, last_name)
                if status_code == 200:
                    clean_form.save()
                    messages.success(
                        request, 'A new enquiry was successfully added to the db')
                    return redirect("frontapp:Success")
                elif status_code == 404:
                    messages.error(
                        request, 'Error 404 has occurred during contactFormView() on  ',date)
                    return redirect("frontapp:Error404")
                else:
                    messages.error(
                        request, 'Sorry, something went wrong sending the email, try again. Status code: ',status_code)
                    return
            else:
                
                messages.error(request, 'The form is invalid and may contain data in the last_name field which is not visible to the user and indicates a Bot has filled it in. This form will not be processed.',date)
        else:
            form = ContactForm()
    context = {'form': form}
    return render(request, 'ContactForm.html', context)            