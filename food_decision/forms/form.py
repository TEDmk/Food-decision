from wtforms import Form, StringField, validators


class TestForm(Form):
    test_field = StringField(label='Essai', validators=[validators.length(min=2, max=25)])
