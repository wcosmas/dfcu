from django.urls import path


from .views import get_loans


urlpatterns = [
    path('', get_loans)
]
