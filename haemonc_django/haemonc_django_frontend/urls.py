from django.urls import path
from .views import VariantEnCreateView

from . import views

app_name = "haemonc_django_frontend" 
urlpatterns = [
    path("", views.index, name="index"),
    path("addVariant", views.create_variant, name="create_variant"),
    path('input_variant', views.variant_input, name='variant_input'),




    ]



