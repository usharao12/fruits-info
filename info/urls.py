
from django.urls import path

from info import views




urlpatterns=[
    path('<int:pk>/',views.fruit_detail,name='fruit_detail'),
]