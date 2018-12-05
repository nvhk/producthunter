from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        if request.POST['haslo1'] == request.POST['haslo2']:]
            User.objects.get(login=request.POST['login'])
    else:
        return render(request, 'konta/login.html')



def rejestracja(request):
    return render(request, 'konta/rejestracja.html')

def wylogowanie(request):
    return render(request, 'konta/zarejestruj.html')
