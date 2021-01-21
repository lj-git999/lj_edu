from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path("banner/",views.BannerAPIView.as_view()),
    path("header/",views.HeaderAPIView.as_view()),
    path("footer/",views.FooterAPIView.as_view()),

]