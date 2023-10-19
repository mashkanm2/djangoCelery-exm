from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import UserChangeForm,userLoginForm,userRegisterationForm
from .models import userAcountModel



class userRegisterView(TemplateView):
    form_class =userRegisterationForm
    template_name='Account/register.html'
    
    def get(self,request):
        form=self.form_class
        return render(request=request,template_name=self.template_name,context={'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd_=form.cleaned_data
            userAcountModel.objects.create_user(user_name=cd_['user_name'],
                                                email=cd_['email'],
                                                phone_number=cd_['phone_number'],
                                                password=cd_['password'])
            messages.success(request, 'you registered.', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form':form})
    
    
class userLoginView(TemplateView):
    form_class=userLoginForm
    template_name='Account/login.html'
    
    def get(self,request):
        form=self.form_class
        return render(request=request,template_name=self.template_name,context={'form':form})
    
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
        return render(request, self.template_name, {'form':form_data})



class userLogoutView(TemplateView):
    def get(self,request):
        logout(request)
        messages.success(request,"you logout successfully ... ",'success')
        return redirect("home:home")
    