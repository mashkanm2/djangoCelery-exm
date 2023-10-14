from django.db import models
from django.urls import reverse

class companyModels(models.Model):
    name_c=models.CharField(max_length=30,unique=True)
    price = models.IntegerField()
    
    class Meta:
        ordering = ('name_c',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name_c
    


class postBlogModel(models.Model):
    company=models.ManyToManyField(companyModels,related_name='postblog')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    best_acc=models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        ordering = ('best_acc',)
        verbose_name = "blogpost"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
