from django.shortcuts import render
from django.views.generic import TemplateView


class FormaView(TemplateView):
    template_name = 'form.html'
