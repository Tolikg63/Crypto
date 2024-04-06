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
        return render(request, 'crypto_shop/about.html')