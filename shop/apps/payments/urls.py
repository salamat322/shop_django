from django.urls import path
from . import views


urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.done_payment, name='done'),
    path('canceled/', views.canceled_payment, name='canceled'),
]