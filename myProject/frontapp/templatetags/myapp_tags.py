from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from django.http import HttpRequest

register = template.Library()

@register.simple_tag()
def get_footer_data(footer_data_url):
    print("Attempting to render template:", footer_data_url)
    request = {}
    print("request: ",request)
    response = render_to_string(footer_data_url, context=request)
    print("Rendered template content:", response)
    return response

@register.simple_tag()
def call_url(url_name):
    print("url name = ",url_name)
    request = {}
    request = reverse(url_name)
    print("reverse url = ",request)
    response = render_to_string(url_name, context=request)
    print("response = ",response)
    return response



