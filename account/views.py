import databases
from rest_framework.views import APIView

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

class lis(APIView):
    def get(self,request):
        serializer=User.objects.all()
        serializer1=RegistrationSerializer(serializer,many=True)
        return Response(serializer1.data)

    def post(self,request):
        serializers2=RegistrationSerializer(data=request.data)
        if serializers2.is_valid():
            serializers2.save()
            return Response({'data':'data save success'})
        return Response({'data':'data not save'})

class lisdetails(APIView):
    def get(self,request,pk,format=None):
        a=User.objects.get(pk=pk)
        b=RegistrationSerializer(a)
        return Response(b.data)

    def put(self,request,pk):
        a=User.objects.get(pk=pk)
        b=RegistrationSerializer(a,data=request.data)
        if b.is_valid():
            b.save()
            return Response({'data1':b.data,'data':'data is update'})
        return Response({'data':'data not update'})

    def delete(self,request,pk):
        a=User.objects.get(pk=pk)
        a.delete()
        return Response({'data':'data delete'})