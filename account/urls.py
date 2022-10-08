from django.urls import path, include
from .views import *

urlpatterns = [
    # path('api/',RegistrtionView.as_view()),
    # path('api/',RegistrtionView1.as_view()),
    # path('api/<int:pk>/',Up.as_view()),
    path('listdetails/<int:pk>/',lisdetails.as_view()),
    # path('listuser/',listUser1.as_view()),
    # path('getuser/<int:id>',GetUser.as_view()),
    # path('alluser/',AllUser.as_view())
]

