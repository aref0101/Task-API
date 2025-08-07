from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class TaskSerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source= 'owner.username')

    class Meta:
        model= Task
        fields= ['id', 'title', 'description', 'is_done', 'owner']


class UserRegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only= True, min_length=  8,
    validators= [validate_password], style= {'input_type': 'password'})

    class Meta:
        model= User
        fields= ('username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)