from django import forms
from django.contrib.auth import get_user_model
from .models import Member

class MemberForm(forms.ModelForm):

   class Meta:
       model = Member
       fields = [ 'first_name','last_name','username', 'email', 'gender', 'dateofbirth', 'image','password']




class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [ 'first_name','last_name','username', 'email', 'gender']


