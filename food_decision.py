from food_decision import app, db
from food_decision.models import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}