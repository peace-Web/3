from django import views
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("order/<str:pk>/", views.order, name='order'),
    path("makeorder/",
         views.makeorder, name="makeorder")
]
