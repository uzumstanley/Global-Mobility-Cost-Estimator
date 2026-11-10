from django.urls import path
from . import views

urlpatterns = [
    path('', views.estimator_view, name='estimator'),
]

