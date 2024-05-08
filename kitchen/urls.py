from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishTypeCreate,
    DishTypeUpdate,
    DishTypeDelete,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookYearsOfExperienceUpdateView,
    CookDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create", DishTypeCreate.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update", DishTypeUpdate.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete", DishTypeDelete.as_view(), name="dish-type-delete"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookYearsOfExperienceUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "kitchen"
