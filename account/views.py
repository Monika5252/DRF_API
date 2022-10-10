import databases
import permission as permission
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from jwt.utils import force_bytes
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import *
from .models import *
from rest_framework import generics, permissions, status,mixins
from rest_framework.response import Response

# class RegistrtionView(generics.GenericAPIView):
#     query=User.objects.all()
#     serializer_class = RegistrationSerializer
#     def post(self,request):
#         serializer=RegistrationSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'msg':'data save success'})
#         else:
#             # return Response({'msg':'data not save'})
#             return Response({'msg':'data not save'})

# class RegistrtionView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#
#
# class listUser1(generics.GenericAPIView,mixins.ListModelMixin):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#
# # class listUser(generics.GenericAPIView):
# #       query=User.objects.all()
# #       serializer_class = RegistrationSerializer
# #       def get(self,request):
# #           serializers=RegistrationSerializer()
# #           return Response(serializers.data)
#
# class GetUser(generics.GenericAPIView,mixins.RetrieveModelMixin):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
# # class AllUser(generics.GenericAPIView,mixins.CreateModelMixin):
# #     queryset = Demo.objects.all()
# #     serializers_class=AllUserSerializer
#
#
# class AllUser(generics.GenericAPIView,APIView):
#     def post(self, request, *args, **kwargs):
#         file_serializer = AllUserSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# using mixin
# class RegistrtionView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request,*args,**kwargs)


# # using generic

# class RegistrtionView1(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#
# class Up(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#

## using api class-based view


# class lis(APIView):
#     def get(self,request):
#         serializer=User.objects.all()
#         serializer1=RegistrationSerializer(serializer,many=True)
#         return Response(serializer1.data)
#
#     def post(self,request):
#         serializers2=RegistrationSerializer(data=request.data)
#         if serializers2.is_valid():
#             serializers2.save()
#             return Response({'data':'data save success'})
#         return Response({'data':'data not save'})
#
# class lisdetails(APIView):
#     def get(self,request,pk,format=None):
#         a=User.objects.get(pk=pk)
#         b=RegistrationSerializer(a)
#         return Response(b.data)
#
#     def put(self,request,pk):
#         a=User.objects.get(pk=pk)
#         b=RegistrationSerializer(a,data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response({'data1':b.data,'data':'data is update'})
#         return Response({'data':'data not update'})
#
#     def delete(self,request,pk):
#         a=User.objects.get(pk=pk)
#         a.delete()
#         return Response({'data':'data delete'})


# simple funtion

# @api_view(["GET"])
# @permission_classes(permissions.IsAdminUser,)
# def alldata(request):
#     b=User.objects.all()
#     c=RegistrationSerializer(b,many=True)
#     return Response(c.data)
#
# @api_view(['POST'])
# def datasave(request):
#     c=RegistrationSerializer(data=request.data)
#     if c.is_valid():
#         c.save()
#         return Response({'data':'data is save success'})
#     return Response({'data':'data is not save'})
#
# @api_view(['PUT'])
# def dataupdate(request,pk):
#     c=User.objects.get(pk=pk)
#     v=RegistrationSerializer(c,data=request.data)
#     if v.is_valid():
#         v.save()
#         return Response({'data':'data is update success'})
#     return Response({'data':'data is not update'})
#
# @api_view(['GET'])
# def datadelete(request,pk):
#     c=User.objects.get(pk=pk)
#     c.delete()
#     return Response({'data':'data is delete'})


class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      # from_email=os.environ.get('EMAIL_FROM'),
      from_email='ranjitshinde9404@gmail.com',
      to=[data['to_email']]
    )
    email.send()

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

def verifymail(user,request):
  uid = urlsafe_base64_encode(force_bytes(user.email))
  print(uid)
  token = PasswordResetTokenGenerator().make_token(user)
  current_site = get_current_site(request)
  domain=current_site.domain
  link = 'http://'+domain+'/validate/' + uid + '/' + token
  print('Validation Link sent', link)
  # Send EMail
  body = 'Click Following Link to verify your Account : ' + link
  data = {
    'subject': 'Validation Email ',
    'body': body,
    'to_email': user.email
  }
  Util.send_email(data)

@permission_classes(permissions.IsAuthenticated,)
@api_view(["GET"])
def alldata(request):
    b=User.objects.all()
    c=RegistrationSerializer(b,many=True)
    return Response(c.data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
@authentication_classes([])
def datacreate(request):
    c=RegistrationSerializer(data=request.data)
    if c.is_valid(raise_exception=True):
        a=c.save()
        verifymail(a,request)
        return Response({'data':'verification mail send your email'})
    return Response({'data':'data is not save'})

@api_view(['PUT'])
@permission_classes([permissions.AllowAny,])
@authentication_classes([])
def dataupdate(request,pk):
    c=User.objects.get(pk=pk)
    v=RegistrationSerializer(c,data=request.data)
    if v.is_valid():
        v.save()
        return Response({'data':'data is update success'})
    return Response({'data':'data is not update'})

@api_view(['GET'])
def datadelete(request,pk):
    c=User.objects.get(pk=pk)
    if c:
        c.delete()
        return Response({'data':'data is delete'})
    else:
        return Response({'data':'data not present'})

class LoginView(generics.GenericAPIView,APIView):
    queryset = User.objects.all()
    serializer_class = Loginserializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = Loginserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            if not user.is_admin:
                verifymail(user, request)
                return Response({'msg': 'Verification link has been sent to your email. Please verify your account'},
                                status=status.HTTP_201_CREATED)
            return Response(
                {'token': token,  'msg': 'Login Success',
                 }, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}},
                            status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([permissions.AllowAny,])
def validate(request,uid,token):
  try:
    id = smart_str(urlsafe_base64_decode(uid))
    print(id)
    user = User.objects.get(email=id)
    if not PasswordResetTokenGenerator().check_token(user, token):
      raise serializers.ValidationError('Token is not Valid or Expired')
    user.is_verify = True
    user.save()
    # return Response({'msg': 'Account is verified Please Login'})
    return HttpResponse('<p>Your account has been successfully verified. Please <a href="http://127.0.0.1:8001/login/">click here</a> to login</p>')
  except DjangoUnicodeDecodeError as identifier:
    PasswordResetTokenGenerator().check_token(user, token)
    raise serializers.ValidationError('Token is not Valid or Expired')