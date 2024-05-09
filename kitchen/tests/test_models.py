from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test_name",
        )
        self.assertEqual(
            str(dish_type),
            dish_type.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 5

        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,

        )
        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.years_of_experience, years_of_experience)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="test_name",
        )
        dish = Dish.objects.create(
            name="test_dish_name",
            price= 0.95,
            dish_type=dish_type,
        )
        self.assertEqual(
            str(dish),
            f"{dish.name} ({dish.price}, {dish.dish_type}, {dish.description})"
        )
