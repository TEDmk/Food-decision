from food_decision import db
from food_decision.models import Recipe, DataRecipe
from food_decision.forms import MealForm, IngredientForm


def create_recipe(data_recipe: DataRecipe):
    return Recipe(
        name=data_recipe.name,
        persons=data_recipe.persons,
        description=data_recipe.description,
        tags=data_recipe.tags,
        total_ingredients=data_recipe.total_ingredients,
        ingredients=data_recipe.ingredients
    )


def create_recipe_from_form(form: MealForm):
    data_recipe = DataRecipe(
        name=form.name.data, persons=form.persons.data,
        description=form.description.data, tags={'tags': form.tags.data},
        total_ingredients=form.total_ingredients.data,
        ingredients={'ingredients': None}
    )
    return create_recipe(data_recipe)


def add_ingredients_to_recipe_from_form(recipe: Recipe, form: IngredientForm):
    for i in form:
        print(i)
