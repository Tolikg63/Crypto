from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View


class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'crypto_shop/index.html')


class How(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'crypto_shop/how.html')
    

class About(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        links = [
            ('link1', "Link 1"),
            ('link2', "Link 2"),
            ('link3', "Link 3"),
            ('link4', "Link 4"),
            ('link5', "Link 5"),
        ]
        context = {
            'links': links
        }
        return render(request, 'crypto_shop/about.html', context=context)