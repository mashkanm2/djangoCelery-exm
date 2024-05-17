

from .models import postBlogModel,companyModels
from rest_framework import serializers

class postBlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = postBlogModel
        fields = ('company','name','slug','best_acc',)

    # def validate_company(self,value):
    #     pass

    # def validate(self, attrs):
    #     return super().validate(attrs)
    
class companyModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyModels
        fields = '__all__'  # or specify fields explicitly