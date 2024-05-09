from django.test import TestCase

from kitchen.forms import (
    DishSearchForm,
    CookCreationForm,
    CookSearchForm,
    DishTypeSearchForm,
)


class TestForms(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            "username": "test",
            "password1": "11!_033s",
            "password2": "11!_033s",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 0,
        }

    def test_cook_creation_form_with_additional_fields(self) -> None:
        form = CookCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

    def test_cook_creation_form_with_years_of_experience(self) -> None:
        for years_of_experience in (
            0,
            15,
            33,
        ):
            self.form_data["years_of_experience"] = years_of_experience
            form = CookCreationForm(data=self.form_data)
            self.assertTrue(form.is_valid())

    def test_dish_type_search_form(self) -> None:
        form = DishTypeSearchForm(data={"name": "test_name"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test_name")

    def test_dish_search_form(self) -> None:
        form = DishSearchForm(data={"name": "test_dish_name"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test_dish_name")

    def test_cook_search_form(self) -> None:
        form = CookSearchForm(data={"username": "test"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "test")
