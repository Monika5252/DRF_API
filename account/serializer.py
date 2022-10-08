
from rest_framework import serializers
from . models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','name','mobile','password']


    def create(self, validate_data):
        return User.objects.create_user(**validate_data)




