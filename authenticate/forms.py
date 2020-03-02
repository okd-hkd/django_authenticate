from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 


class SignUpForm(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length = 100)
  last_name = forms.CharField(max_length = 100)
  fav_color = forms.CharField(max_length = 100)
  
  class Meta:
      model = User
      fields = ('username','first_name','last_name','email','password1','password2','fav_color')


# class ProfileForm(forms.ModelForm):
#   class Meta:
#       model = Profile
#       fields = ('bio', 'location', 'birth_date')