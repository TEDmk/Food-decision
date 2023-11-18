from flask import render_template, flash, redirect, url_for
from sqlalchemy import update

from food_decision import app, db
from food_decision.forms import MealForm, IngredientForm
from food_decision.models import Recipe, DataRecipe
from food_decision.services.recipe import create_recipe_from_form, get_new_ingredients


@app.route('/')
@app.route('/index')
def index():
    recipes: list[Recipe] = db.session.query(Recipe).all()
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
    recipe_to_update = db.session.query(Recipe).get_or_404(ident=recipe_id)
    form = IngredientForm()
    if form.validate_on_submit():
        new_ingredients = get_new_ingredients(recipe_to_update, form)
        db.session.query(Recipe).filter(Recipe.id == recipe_to_update.id).update(
            {"ingredients": new_ingredients}
        )
        db.session.commit()
        flash('Congratulations an ingredient has been added to the recipe!')
        return redirect(url_for('add_ingredient', recipe_id=recipe_id))
    return render_template('add_ingredient.html', title='Add ingredient', form=form, recipe=recipe_to_update)


@app.route('/recipe/<recipe_id>', methods=['GET'])
def recipe(recipe_id):
    wanted_recipe = db.session.query(Recipe).get_or_404(ident=recipe_id)
    return render_template('recipe.html', title='Recipe details', recipe=wanted_recipe)
