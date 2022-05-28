from django.urls import path
from cars.views import HomeView
from form.views import FormaView

app_name = 'homes'

urlpatterns = [
    path('', FormaView.as_view(), name="form"),
]