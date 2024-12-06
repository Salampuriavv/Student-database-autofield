from rest_framework import serializers
from .models import Student, StudentPNo

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentPNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPNo
        fields = '__all__'
