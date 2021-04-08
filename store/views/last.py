from django.views import View
from django.shortcuts import render, redirect

class Last(View): 
    def get(self, request):
        return render(request , 'last.html')