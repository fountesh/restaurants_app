from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from menu.models import Dish

# Create your views here.

class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return Review.objects.filter(dish_id=self.kwargs["dish_id"], status=Review.Status.APPROVED)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.dish = get_object_or_404(Dish, id=self.kwargs["dish_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("dish_detail", kwargs={"pk": self.kwargs["dish_id"]})