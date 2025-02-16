from django.urls import path
from .views import OrderHistoryView, ReorderView

urlpatterns = [
    path("history/", OrderHistoryView.as_view(), name="order_history"),
    path("reorder/<int:order_id>/", ReorderView.as_view(), name="reorder"),
]