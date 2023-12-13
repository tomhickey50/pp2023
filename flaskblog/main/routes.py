from flask import render_template, request, Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required
from flaskblog import db
from flaskblog.models import Workout, Post
from flaskblog.main.forms import EnterWorkoutForm
from datetime import datetime

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/enter_workout", methods=['GET', 'POST'])
@login_required
def workout(): 
    form = EnterWorkoutForm()
    if form.validate_on_submit():
        year,month,day = form.date_posted.raw_data[0].split('-')
        workout = Workout(date_posted=datetime(int(year),int(month),int(day)), total_load=form.total_load.data)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been entered!', 'success')
        return redirect(url_for('main.home'))
    return render_template('workout_tracker.html', form=form, legend='Enter Workout')

@main.route("/workout_viewer")
def view_workout():
    workouts = Workout.query.order_by(Workout.date_posted.desc())
    return render_template('workout_viewer.html', workouts=workouts, legend='View Workout')