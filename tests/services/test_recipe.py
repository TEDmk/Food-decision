from food_decision.services.recipe import create_recipe, create_recipe_from_form
from food_decision.models import Recipe, DataRecipe
from food_decision.forms import MealForm


def test_create_recipe():
    test_recipe_data = DataRecipe(
        name='test', persons=2, description='This is a test Recipe',
        tags={'tags': ['tag1', 'tag2']},
        ingredients={
            'ingredient': ''
        }
    )
