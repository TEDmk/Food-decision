from flask import render_template, flash, redirect, url_for
from food_decision import app, db
from food_decision.forms import MealForm, IngredientForm
from food_decision.models import Recipe, DataRecipe
from food_decision.services.recipe import create_recipe_from_form, add_ingredients_to_recipe_from_form


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
        return redirect(url_for('add_ingredients', recipe_id=new_recipe.id))
    return render_template('add_recipe.html', title='Add recipe', form=form)


@app.route('/add_ingredients/<recipe_id>', methods=['GET', 'PATCH'])
def add_ingredients(recipe_id):
    recipe = Recipe.query.get_or_404(ident=recipe_id)
    form = IngredientForm()
    if form.validate_on_submit():
        add_ingredients_to_recipe_from_form(recipe, form)
        db.session.add(recipe)      # Voir comment faire un PATCH en FLASK (adapter html si besoin)
        db.session.commit(recipe)   # FAIRE TESTS !!!
        flash('Congratulations a new recipe and its ingredients has been added!')
        return redirect(url_for('index'))
    return render_template('add_ingredients.html', title='Add ingredients', form=form, recipe=recipe)


@app.route('/recipe/<recipe_id>', methods=['GET'])
def recipe(recipe_id):
    print('\n RECIPE ID ', type(recipe_id), '\n')
    wanted_recipe = Recipe.query.get_or_404(ident=recipe_id)
    return render_template('recipe.html', title='Recipe details', recipe=wanted_recipe)
