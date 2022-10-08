from django.urls import path, include
# from .views import
from . import  views

urlpatterns = [
    # path('api/',RegistrtionView.as_view()),
    # path('api/',RegistrtionView1.as_view()),
    # path('api/<int:pk>/',Up.as_view()),
    # path('listdetails/<int:pk>/',lisdetails.as_view()),
    # path('listuser/',listUser1.as_view()),
    # path('getuser/<int:id>',GetUser.as_view()),
    # path('alluser/',AllUser.as_view())


    # with only funtion
    path('alldata/',views.alldata),
    path('datacreate/',views.datacreate),
    path('dataupdate/<int:pk>/',views.dataupdate),
    path('datadelete/<int:pk>/',views.datadelete),

]

