from food_decision import db
from food_decision.models import Recipe, DataRecipe
from food_decision.forms import MealForm, IngredientForm


def create_recipe(data_recipe: DataRecipe):
    return Recipe(
        name=data_recipe.name,
        persons=data_recipe.persons,
        description=data_recipe.description,
        tags=data_recipe.tags,
        ingredients=data_recipe.ingredients
    )


def create_recipe_from_form(form: MealForm):
    data_recipe = DataRecipe(
        name=form.name.data, persons=form.persons.data,
        description=form.description.data, tags={'tags': form.tags.data},
        ingredients={'ingredients': None}
    )
    return create_recipe(data_recipe)


def add_ingredient_to_recipe_from_form(recipe_to_update: Recipe, form: IngredientForm):
    ingredients = recipe_to_update.ingredients['ingredients']
    new_ingredients = [form.ingredient_name.data, form.ingredient_quantity.data, form.ingredient_unit.data]
    if ingredients:
        ingredients.append(new_ingredients)
        print('\n type ', type(ingredients), '\n')
        ingredients = {'ingredients': ingredients}
    else:
        ingredients = {'ingredients': [new_ingredients]}
    recipe_to_update.ingredients = ingredients
    return recipe_to_update
