from flask import render_template, flash, redirect, url_for
from food_decision import app, db
from food_decision.forms import MealForm
from food_decision.models import Recipe


@app.route('/')
@app.route('/index')
def index():
    recipes: list[Recipe] = Recipe.query.all()
    return render_template('index.html', title='Home', recipes=recipes)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = MealForm()
    if form.validate_on_submit():
        new_meal = Recipe(
            name=form.name.data,
            description=form.description.data,
            tags={'tags': form.tags.data}
        )
        db.session.add(new_meal)
        db.session.commit()
        flash('Congratulations a new meal has been added!')
        return redirect(url_for('index'))
    return render_template('add.html', title='Add meal', form=form)


@app.route('/recipe/<recipe_id>', methods=['GET'])
def recipe(recipe_id):
    print('\n RECIPE ID ', type(recipe_id), '\n')
    wanted_recipe = Recipe.query.get_or_404(ident=recipe_id)
    return render_template('recipe.html', title='Recipe details', recipe=wanted_recipe)
