from django.urls import path
from . import views

urlpatterns = [
    path('response/', views.response_test, name='response'),
    path('template1/', views.template_test_1, name='template'),
    path('template2/', views.template_test_2, name='template'),

]
