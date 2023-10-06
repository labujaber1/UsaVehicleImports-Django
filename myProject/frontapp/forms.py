from django.forms import ModelForm, Textarea
from .models import GeneralEnquiry


class ContactForm(ModelForm):
    class Meta:
        model = GeneralEnquiry
        fields = ["name", "from_email", "phone_number", "subject", "enquiry"]
        widgets = {"enquiry": Textarea(attrs={"cols": 80, "rows": 5}), }


form = ContactForm()
