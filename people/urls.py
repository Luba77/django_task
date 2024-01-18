from django.urls import path
from .views import TeamListCreateView, TeamDetailView, PersonListCreateView, PersonDetailView

urlpatterns = [
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('person/', PersonListCreateView.as_view(), name='person-list-create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]

