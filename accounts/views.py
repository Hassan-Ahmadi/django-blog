from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm

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
            else:
                messages.add_message(request, 50, "A serious error occurred.")
                

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
            print('Form is valid!')
            form.save()
            print('Form saved!')
            # return reverse('accounts:login')
            return redirect(reverse('accounts:login'))
        else:
            
            print('Form is not valid!', form.error_messages)
            messages.error(request, messages.ERROR, f'Failed to create account. {form.error_messages}')
        
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

# def reset_password_view(request):
#     # if not already logged in
#     if request.user.is_authenticated:
#         return redirect('/')
    
#     # # else way let the user signup
#     if request.method == "POST":
#         return render(request, 'accounts/reset-password-done.html')
#     #     form = UserCreationForm(request.POST)        
#     #     if form.is_valid():
#     #         print('Form is valid!')
#     #         form.save()
#     #         print('Form saved!')
#     #         # return reverse('accounts:login')
#     #         return redirect(reverse('accounts:login'))
#     #     else:
            
#     #         print('Form is not valid!', form.error_messages)
#     #         messages.error(request, messages.ERROR, f'Failed to create account. {form.error_messages}')
        
#     # form = UserCreationForm()
#     # context = {}
#     return render(request, 'accounts/reset-password.html')