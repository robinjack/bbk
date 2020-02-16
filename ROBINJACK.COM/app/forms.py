from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class SubmitAnything(FlaskForm):
    submission = StringField('What do you want to say?', validators=[DataRequired()])