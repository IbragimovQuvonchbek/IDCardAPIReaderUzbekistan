from django.urls import path
from .views import ClientIDCardViewSet

urlpatterns = [
    path('idcard/', ClientIDCardViewSet.as_view())
]
