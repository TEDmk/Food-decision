from flask import render_template, flash, redirect, url_for
from sqlalchemy import update

from food_decision import app, db
from food_decision.forms import MealForm, IngredientForm
from food_decision.models import Recipe, DataRecipe
from food_decision.services.recipe import create_recipe_from_form, add_ingredient_to_recipe_from_form


@app.route('/')
@app.route('/index')
def index():
    recipes: list[Recipe] = Recipe.query.all()
    return render_template('index.html', title='Home', recipes=recipes)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    form = MealForm()
    if form.validate_on_submit():
        new_recipe = create_recipe_from_form(form)
        db.session.add(new_recipe)
        db.session.commit()
        flash('Congratulations a new recipe has been added!')
        return redirect(url_for('add_ingredient', recipe_id=new_recipe.id))
    return render_template('add_recipe.html', title='Add recipe', form=form)


@app.route('/add_ingredient/<recipe_id>', methods=['GET', 'POST'])
def add_ingredient(recipe_id):
    recipe_to_update = Recipe.query.get_or_404(ident=recipe_id)
    print('\n RECIPE INGREDIENTS FIRST ', recipe_to_update.ingredients, '\n')
    form = IngredientForm()
    if form.validate_on_submit():
        recipe_updated = add_ingredient_to_recipe_from_form(recipe_to_update, form)
        print('\n RECIPE UPDATED BEFORE COMMIT ', recipe_updated.ingredients, '\n')
        # db.session.refresh(recipe_updated)
        db.session.commit()
        recipe_updated_2 = Recipe.query.get_or_404(ident=recipe_id)
        print('\n RECIPE INGREDIENTS AFTER COMMIT ', recipe_updated_2.ingredients, '\n')
        flash('Congratulations an ingredient has been added to the recipe!')
        return redirect(url_for('add_ingredient', recipe_id=recipe_id))
    return render_template('add_ingredient.html', title='Add ingredient', form=form, recipe=recipe_to_update)


@app.route('/recipe/<recipe_id>', methods=['GET'])
def recipe(recipe_id):
    wanted_recipe = Recipe.query.get_or_404(ident=recipe_id)
    return render_template('recipe.html', title='Recipe details', recipe=wanted_recipe)
