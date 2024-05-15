from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.core.exceptions import PermissionDenied

from .models import DishType, Cook, Dish
from .forms import (
    DishTypeSearchForm,
    CookSearchForm,
    CookCreationForm,
    CookYearsOfExperienceUpdateForm, DishSearchForm, DishForm,
)


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1
    }

    return render(request, "kitchen/index.html", context=context)


class AdminRequiredMixin:
    """Verify that the current user is an admin."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")

    def get_context_data(self, **kwargs):
        context = super(DishTypeCreateView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")

    def get_context_data(self, **kwargs):
        context = super(DishTypeUpdateView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")

    def get_context_data(self, **kwargs):
        context = super(DishTypeDeleteView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )

        return queryset


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm

    def get_context_data(self, **kwargs):
        context = super(CookCreateView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class CookYearsOfExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookYearsOfExperienceUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")

    def get_context_data(self, **kwargs):
        context = super(CookYearsOfExperienceUpdateView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")

    def get_context_data(self, **kwargs):
        context = super(CookDeleteView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(initial={"name": name})
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")

    def get_context_data(self, **kwargs):
        context = super(DishCreateView, self).get_context_data(**kwargs)
        context["is_admin"] = self.request.user.is_staff  # Pass admin status to the template
        return context


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class ToggleAssignToDishView(LoginRequiredMixin, generic.View):
    model = Dish
    def post(self, request, pk):
        cook = Cook.objects.get(id=request.user.id)
        if Dish.objects.get(id=pk) in cook.dishes.all():
            cook.dishes.remove(pk)
        else:
            cook.dishes.add(pk)
        return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", args=[pk]))
