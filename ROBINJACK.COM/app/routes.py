from flask import render_template, flash, redirect, url_for
from app import app, db, models
from app.forms import SubmitAnything


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SubmitAnything()
    messages = models.Message.query.all()
    if form.validate_on_submit():
        flash("Thanks for saying something!")
        m = models.Message(message=form.submission.data)
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', messages=messages, form=form)






@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SubmitAnything()
    if form.validate_on_submit():
        flash("Thanks for saying something!")
        m = models.Message(message=form.submission.data)
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html', title='Submit your thoughts', form=form)