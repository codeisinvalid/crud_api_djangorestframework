from rest_framework import serializers
from .models import Student
import re

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    grade = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length= 100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats Full. No new admissions avaliable currently")
        return value
    
    def validate_name(self, value):
        pattern = r'^[a-zA-Z\s]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Name should only contain appnabets or spaces")
        return value



    

