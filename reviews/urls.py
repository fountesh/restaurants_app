from django.urls import path
from .views import ReviewListView, ReviewCreateView

urlpatterns = [
    path("dish/<int:dish_id>/reviews/", ReviewListView.as_view(), name="review_list"),
    path("dish/<int:dish_id>/review/add/", ReviewCreateView.as_view(), name="add_review"),
]
