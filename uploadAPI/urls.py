from django.urls import path
from uploadAPI.views import proListView,proDetailView

urlpatterns = [
path('profile/', proListView.as_view(), name='pro-list'),
path('profile/<int:pk>', proDetailView.as_view(), name='pro-detail'),
]