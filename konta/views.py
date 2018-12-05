from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    return render(request, 'konta/login.html')

def rejestracja(request):
        if request.method == 'POST':
            if request.POST['haslo1'] == request.POST['haslo2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'konta/rejestracja.html', {'error':'User zajety'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['haslo1'])
                    auth.login(request,user)
                    return redirect ('home')
            else:
                return render(request, 'konta/rejestracja.html', {'error':'ZLE HASLO DRUGIE ABO PIERSZE EE'})
        else:
            return render(request, 'konta/rejestracja.html')

def wylogowanie(request):
    return render(request, 'konta/zarejestruj.html')
