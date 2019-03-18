"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import Profile
from app.models import UserProfile
import datetime
import os
from werkzeug.utils import secure_filename

path = app.config['UPLOAD_FOLDER']

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profiles')
def profiles():
    profiles = db.session.query(UserProfile).all()
    return render_template('profiles.html', profiles = profiles)

@app.route('/profile/<int:userid>')
def show_profile(userid):
    user = db.session.query(UserProfile).get(userid)
    return render_template('show_profile.html', user=user)

@app.route('/profile', methods=['GET','POST'])
def profile():
    profile = Profile()

    if request.method == 'POST' and profile.validate_on_submit():
        file = profile.dp.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))
        
        user = UserProfile(
            request.form['firstname'],
            request.form['lastname'],
            request.form['email'],
            request.form['location'],
            request.form['gender'],
            request.form['biography'],
            filename,
            datetime.datetime.now().strftime("%B %d, %Y")
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Profile Saved', 'success')
        return redirect(url_for("profiles")) 
    return render_template("profile.html", form=profile)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
