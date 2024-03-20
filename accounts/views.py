from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')                    

    return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    # if not already logged in
    if request.user.is_authenticated:
        return redirect('/')
    
    # else way let the user signup
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return reverse('accounts:login')
            return redirect('/')
        else:
            messages.error(request, messages.ERROR, 'Failed to create account. Please try again.')            
        
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)