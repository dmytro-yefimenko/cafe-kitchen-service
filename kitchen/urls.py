from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishTypeCreate,
    DishTypeUpdate,
    DishTypeDelete,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create", DishTypeCreate.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/update", DishTypeUpdate.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete", DishTypeDelete.as_view(), name="dish-type-delete"),
]

app_name = "kitchen"
