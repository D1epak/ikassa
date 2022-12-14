from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

class Landing(TemplateView):
    template_name = 'landing-page.html'

    def get_context_data(self, **kwargs):
        table = models.LandingCurse.objects.all()
        context = super().get_context_data(**kwargs)
        context['table'] = table
        return context