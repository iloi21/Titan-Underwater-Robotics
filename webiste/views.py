from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='template')

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/timeline')
def timeline():
    return render_template('timeline.html')

@views.route('/members')
def members():
    return render_template('members.html')

@views.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')
