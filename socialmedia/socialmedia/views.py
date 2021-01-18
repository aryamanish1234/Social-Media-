from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = 'Hello world'

    contaxt = {
        'user': user,
        'hello': hello,
    }
    return render(request,'social/home.html', contaxt)