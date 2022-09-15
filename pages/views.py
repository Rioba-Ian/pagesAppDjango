from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name: str = 'home.html'


class AboutPageView(TemplateView):
    template_name: str = 'about.html'
