from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = "student/home.html"