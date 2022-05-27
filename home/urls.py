from django.urls import path
from cars.views import HomeView
from home.views import FormaView

app_name = 'homes'

urlpatterns = [
    path('', FormaView.as_view(), name="form"),
]