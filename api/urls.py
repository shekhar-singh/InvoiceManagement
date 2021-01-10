from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('getDigitizationStatus/<int:fid>', views.getDigitizationStatus, name='getDigitizationStatus'),
    path('getInvoice/<int:fid>', views.getInvoice, name='getInvoice'),
    path('addInvoice', views.addInvoice, name='addInvoice'),
    path('markDigitized', views.markDigitized, name='markDigitized'),
    

]
