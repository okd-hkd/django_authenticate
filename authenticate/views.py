from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm # ProfileForm
from django.contrib import messages
# from django.db import transaction


# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html',{})

# def profile(request):
#     return render(request, 'authenticate/profile.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)

          #  The messages framework allows you to temporarily store messages in one request and retrieve them for display in a subsequent request
          messages.success(request, 'you have been logged in!')
          
          return redirect('home')
        else:
          
          messages.success(request, 'Error logging in - Please try again')
          return redirect ('login')

    else:
      return render(request, 'authenticate/login.html',{})


def logout_user(request):
  logout(request)
  messages.success(request, 'You have been logged out')
  return redirect('home')


def register_user(request):
    user = SignUpForm(request.POST or None)
    # profile_form = ProfileForm(request.POST or None)
    if request.method == 'POST':
      # profile_form = ProfileForm(request.POST, instance=request.user.profile)
      if user.is_valid():
        # user = user_form.save()
        # user.is_active = True
        user.save()


        # profile = profile_form.save(commit=False)
        # profile.user = user
        # profile.save()

        username = user.cleaned_data['username']
        password = user.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, ('You Have Successfully Registered.'))
        return redirect('home')
          
    else:
        user = SignUpForm()
        # # profile_form = ProfileForm(request.POST, instance=request.user.profile)
         
    context = {"form": user}
    return render(request, 'authenticate/register.html', context)

""" 
@login_required
    If the user is logged in, execute the view normally. 

@transaction.atomic
    Atomicity is the defining property of database transactions. 
    atomic allows   us to create a block of code 
    within which the atomicity on the database is guaranteed. 
    If the block of code is successfully completed, 
    the changes are committed to the database.
    If there is an exception, the changes are rolled back.

# """

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = SignUpForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = SignUpForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'authenticate/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })