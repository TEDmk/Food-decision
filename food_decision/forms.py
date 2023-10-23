from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField, IntegerField
from wtforms.validators import DataRequired, NumberRange

from food_decision.enums import Tags


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
    ingredient_key = StringField('Ingredient', validators=[DataRequired()])
    ingredient_value = StringField('Quantity', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', choices=[tag.value for tag in Tags], validators=[DataRequired()])
    submit = SubmitField('Add')

