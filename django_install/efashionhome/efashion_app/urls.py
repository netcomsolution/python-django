from django.urls import path
from .views import v_home_page

urlpatterns = [
    path('', v_home_page)
]