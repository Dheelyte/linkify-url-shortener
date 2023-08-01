from django.urls import path
from .views import ShortenLink, RedirectLink

urlpatterns = [
    path('', ShortenLink.as_view(), name='shorten'),
    path('<slug:id>/', RedirectLink.as_view(), name='redirect'),
]
