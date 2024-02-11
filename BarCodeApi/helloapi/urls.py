from django.urls import path
from . import views

path=[
        path('api/code/',views.barcode.as_view(),name='api'),
        path('api/allcode/<int:pk>',views.bar_code.as_view(),name='retriveupdate'),
]