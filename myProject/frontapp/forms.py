from django.forms import ModelForm, Textarea
from .models import Comment, GeneralEnquiry, Post


class ContactForm(ModelForm):
    class Meta:
        model = GeneralEnquiry
        fields = ["name", "email", "phone_number", "subject", "enquiry"]
        widgets = {"enquiry": Textarea(attrs={"cols": 60, "rows": 5}), }

form = ContactForm()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ "name","body"]
        widgets = {"body": Textarea(attrs={"cols": 50, "rows": 5}), }
        
form = CommentForm()

class LikeForm(ModelForm):
    class Meta:
        model = Post 
        fields = ["likes"]
form = LikeForm() 