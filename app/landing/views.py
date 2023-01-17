from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from .parser.parser import parse


class Landing(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        parse_data = parse()
        print(parse_data)
        table = models.LandingCurse.objects.all()
        table_first = models.LandingCurse.objects.get(value=True)
        seotags = models.SeoTag.objects.all()
        context = super().get_context_data(**kwargs)
        context['table'] = table
        context['tablef'] = table_first
        context['banks'] = parse_data
        context['seotags'] = seotags
        return context
