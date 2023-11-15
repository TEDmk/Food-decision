from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

from food_decision.enums import Tags, Units


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')


class MealForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    persons = IntegerField(
        'Quantity of persons',
        validators=[
            DataRequired(), NumberRange(1, 10, "1 to 10 persons")
        ],
        default=1
    )
    total_ingredients = IntegerField(
        'Quantity of ingredients',
        validators=[
            DataRequired(), NumberRange(1, 25, "1 to 25 ingredients")
        ],
        default=1
    )
    tags = SelectMultipleField('Tags', choices=[tag.value for tag in Tags], validators=[DataRequired()])
    submit = SubmitField('Add')


class IngredientForm(FlaskForm):
    ingredient_name = StringField('Ingredient', validators=[DataRequired()])
    ingredient_quantity = StringField('Quantity', validators=[DataRequired()])
    ingredient_unit = SelectField('Unit', choices=[unit.value for unit in Units], validators=[DataRequired()])
    submit = SubmitField('Add Ingredients')
