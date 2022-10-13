# import random
import datetime
import json
import random

import requests
from rest_framework import serializers
from . models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','name','mobile','password']


    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class Loginserializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=200)
    class Meta:
        model=User
        fields=['email','password']


class  UserLoginOTPSendMobViewSerializer(serializers.Serializer):
  phoneno = serializers.CharField(max_length=10)
  class Meta:
    fields = ['phoneno']

  def validate(self, attrs):
    phoneno = attrs.get('phoneno')
    if len(str(phoneno))!=10:
      raise serializers.ValidationError("Mobile Number should be 10 digit")
    if User.objects.filter(mobile=phoneno).exists():
      user = User.objects.filter(mobile= phoneno).first()
      print(user)
      # tup=OtpManager.objects.get_or_create(userId=user)
      # otpdata=tup[0]
      # if otpdata.motp_counter<2:
      #   otpdata.motp_counter+=1
      #   otpdata.save()
      # elif otpdata.motp_counter==2:
      #   otpdata.motp_counter=3
      #   otpdata.motp_timer=django.utils.timezone.now()+datetime.timedelta(hours=24)
      #   otpdata.save()
      # else:
      #   if otpdata.motp_timer<django.utils.timezone.now():
      #     otpdata.motp_counter = 1
      #     otpdata.motp_timer=None
      #     otpdata.save()
      #   else:
      #     raise serializers.ValidationError(f'You have reached maximum otp limit,Try after {otpdata.motp_timer}')

      otp=random.randint(1000,9999)
      url = "https://www.fast2sms.com/dev/bulkV2"

      # create a dictionary
      my_data = {
        'sender_id': 'FSTSMS',
        'message': str(otp)+' for logging in chintay.com. \nOTP valid for 5 mins. \nPlease do not share this OTP.',
        'language': 'english',
        'route': 'p',
        'numbers': phoneno
      }
      headers = {
        # 'authorization': 'yfrZAGeUvulowXHIFaSihs9cW0Jtd352PCjnmBx4OQpqMTkVDRzOdgaZAivjG2MnRX7u4pyQbFrS6LWs',
        'authorization': 'yfrZAGeUvulowXHIFaSihs9cW0Jtd352PCjnmBx4OQpqMTkVDRzOdgaZAivjG2MnRX7u4pyQbFrS6LWs',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
      }
      response = requests.request("POST", url, data=my_data, headers=headers)
      returned_msg = json.loads(response.text)
      # print the send message
      # print(returned_msg['message'])
      print('mobile otp sent')
      # tim = django.utils.timezone.now()+datetime.timedelta(minutes=1)
      # user.expired_time = tim
      # user.otp=otp
      # user.save()
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')

# class UserLoginThrOTPMobViewSerializer(serializers.Serializer):
#   phoneno=serializers.CharField(max_length=10)
#   otp= serializers.IntegerField()
#   class Meta:
#     model=User
#     fields = ['otp','phoneno']
#
#   def validate(self, attrs):
#     otp = attrs.get('otp')
#     phoneno = attrs.get('phoneno')
#     user = User.objects.filter(mobile=phoneno).first()
#   #   # t1=(user.expired_time).timestamp()
#   #   # t2 = django.utils.timezone.now()
#   #   # if t2 > t1:
#   #   #   raise serializers.ValidationError("OTP has expired")
#   #   # if user.otp == otp:
#   #   #   user.otp = 0000
#   #   #   user.save()
#   #   #   return attrs
#   #   # raise serializers.ValidationError("OTP is not correct")
#   #
#   def create(self, validate_data):
#     user=User.objects.filter(mobile=validate_data['phoneno']).first()
#     return user
