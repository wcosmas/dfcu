from django.urls import path


from .views import get_loans, simulate


urlpatterns = [
    path('', get_loans),
    path('simulate_request/', simulate)
]
