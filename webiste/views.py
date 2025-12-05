from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__, template_folder='template')

@views.route('/')
def index():
    return redirect(url_for('views.home'))

@views.route('/home')
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
