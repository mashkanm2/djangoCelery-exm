from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import userAcountModel

class userCreateForm(forms.Form):
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='conform password',widget=forms.PasswordInput)
    
    class Meta:
        model = userAcountModel
        fields = ('user_name', 'email','phone_number')
        
    
    def clean_password2(self):
        cl_data=self.cleaned_data
        if cl_data['password1'] and cl_data['password2']:
            if cl_data['password1']!=cl_data['password2']:
                raise ValidationError('passwords not match')
            return cl_data['password2']
        else:
            raise ValidationError('passwords is empty')
        
    def save(self,commit=True):
        user=super.save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")

    class Meta:
        model = userAcountModel
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')
        

class userRegisterationForm(forms.Form):
    user_name=forms.CharField(max_length=30,label='user_name')
    email=forms.EmailField()
    phone_number=forms.CharField(max_length=11,label='phone number')
    full_name=forms.CharField(label='full name',max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email=self.cleaned_data['email']
        user=userAcountModel.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError("this email already exists")
        return email
    
    def clean_phone_number(self):
        phone_number=self.cleaned_data['phone_number']
        user=userAcountModel.objects.filter(phone_number=phone_number).exists()
        if user:
            raise forms.ValidationError('phone nuber already exists.')
        return phone_number
    
    def clean_user_name(self):
        user_name=self.cleaned_data['user_name']
        user=userAcountModel.objects.filter(user_name=user_name).exists()
        if user:
            raise forms.ValidationError('user name exists.')
        return user_name
    
    
class userLoginForm(forms.Form):
    user_name=forms.CharField(max_length=30,label='user name')
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    
    
        
