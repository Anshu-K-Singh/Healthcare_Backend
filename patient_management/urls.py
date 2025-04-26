from django.urls import path
from .views import PatientListCreateView, PatientDetailView, MappingListCreateView, MappingDetailView

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patient-list-create'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),
]