from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish

INDEX_URL = reverse("kitchen:index")
DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
COOK_LIST_URL = reverse("kitchen:cook-list")
DISH_LIST_URL = reverse("kitchen:dish-list")


class PublicKitchenTest(TestCase):
    def test_login_required(self):
        response_index = self.client.get(INDEX_URL)
        response_manufacturer = self.client.get(DISH_TYPE_LIST_URL)
        response_driver = self.client.get(COOK_LIST_URL)
        response_car = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(response_index.status_code, 200)
        self.assertNotEqual(response_manufacturer.status_code, 200)
        self.assertNotEqual(response_driver.status_code, 200)
        self.assertNotEqual(response_car.status_code, 200)


class PrivateKitchenTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(
            name="test_manufacturer",
        )
        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(response.status_code, 200)

        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types),
        )

        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_retrieve_cook(self) -> None:
        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)

        cooks = get_user_model().objects.all()
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_retrieve_dish(self) -> None:
        dish_type = DishType.objects.create(
            name="test_manufacturer",
        )
        Dish.objects.create(name="test_name", price=0.49, dish_type=dish_type)
        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
