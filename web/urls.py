from django.conf.urls import url
from web import views






urlpatterns = [
    url(r'^index/', views.index),
    url(r'^list/', views.list),
]
