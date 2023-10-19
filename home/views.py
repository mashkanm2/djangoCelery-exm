from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.views import View
from .models import postBlogModel,companyModels

class postBlogView(View):
    template_name='home/detail.html'
    
    def get(self,request,slug):
        postBlog=get_object_or_404(postBlogModel,slug=slug)
        return render(request,self.template_name,{'product':postBlog})
    
    def post(self,request):
        pass
    


class homeView(View):
    template_name = 'home/home.html'
    
    def get(self,request,company_slug=None):
        posts=postBlogModel.objects.all()
        companys=companyModels.objects.all()
        if company_slug:
            cmps=companyModels.objects.get(slug__icontains=company_slug)
            posts=posts.filter(company=cmps)
            
        return render(request,self.template_name,{'products':posts, 'companyes':companys})
        
        