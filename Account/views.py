from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserChangeForm,userLoginForm,userRegisterationForm
from .models import userAcountModel



class userRegisterView(View):
    form_ =userRegisterationForm
    template_n='Account/register.html'
    
    def get(self,request):
        return render(request=request,template_name=self.template_n,context={'form':self.form_})
    
    def post(self,request):
        form_data=self.form_(request.POST)
        if form_data.is_valid():
            cd_=form_data.cleaned_data
            userAcountModel.objects.create_user(user_name=cd_['user_name'],
                                                email=cd_['email'],
                                                phone_number=cd_['phone_number'],
                                                password=cd_['password'])
            messages.success(request, 'you registered.', 'success')
            return redirect('home:home')
        return render(request, self.template_n, {'form':self.form_})
    
    
class userLoginView(View):
    form_class=userLoginForm
    template_n='Account/login.html'
    
    def get(self,request):
        return render(request=request,template_name=self.template_n,context={'from':self.form_class})
    
    def post(self,request):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            cd_=form_data.cleaned_data
            user=authenticate(request=request,user_name=cd_['user_name'],password=cd_['password'])
            if user is not None:
                login(request=request,user=user)
                messages.success(request,"you login successfully ..",'success')
                return redirect('home:home')
            
            messages.error(request, 'phone or password is wrong', 'warning')
        return render(request, self.template_name, {'form':self.form_class})



class userLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"you logout successfully ... ",'success')
        return redirect("home:home")
    