from django.shortcuts import render,redirect,get_list_or_404
from django.views import View
from .models import postBlogModel,companyModels

class postBlogView(View):
    template_name='home/detail.html'
    
    def get(self,request,slug):
        postBlog=get_list_or_404(postBlogModel,slug=slug)
        return render(request,self.template_name,{'product':postBlog})
    
    def post(self,request):
        pass
    


class homeView(View):
    template_name = 'home/home.html'
    
    def get(self,request,company=None):
        posts=postBlogModel.objects.all()
        companys=companyModels.objects.all()
        if company:
            cmps=companys.filter(name_c__icontains=company)
            posts=posts.filter(company=cmps)
            
        return render(request,self.template_name,{'products':posts, 'categories':companys})
        
        

