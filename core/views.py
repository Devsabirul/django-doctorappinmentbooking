from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Home(View):
    template_name = ''

    def get(self, request, *arge):
        return render(request, self.template_name)


class Searchdoctor(View):
    template_name = ''

    def get(self, request, *arge):
        return render(request, self.template_name)
