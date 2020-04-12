from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_value':"Welcome from Safe Envionment"}
    return render(request,'environmentApp/index.html',context=my_dict)
