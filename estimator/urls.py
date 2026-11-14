# Routes the root URL to `estimator_view`.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.estimator_view, name='estimator'),
]

