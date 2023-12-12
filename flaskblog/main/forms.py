from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired

class EnterWorkoutForm(FlaskForm):
	date_posted = DateField('Date', validators=[DataRequired()])
	total_load = IntegerField('Total Load Lifted', validators=[DataRequired()])
	submit = SubmitField('Post')