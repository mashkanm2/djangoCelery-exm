

from rest_framework import serializers

# class InputDataSerializer(serializers.Serializer):
#     company_name = serializers.CharField(max_length=255)
#     win_size = serializers.IntegerField()
#     csv_file = serializers.FileField()

class InputFilesSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=255)
    win_size = serializers.IntegerField()
    csv_file = serializers.FileField()

class AppendInputFilesSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=255)
    csv_file1 = serializers.FileField()
    csv_file2 = serializers.FileField()
