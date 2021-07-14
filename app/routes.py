from app import application,models
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,jsonify

@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html',title='About Me',pos='home')

@application.route('/projects')
def projects():
    return render_template('projects.html',title='Projects',pos='projects')

@application.route('/contacts')
def contacts():
    return render_template('contacts.html',title='contacts',pos='contacts')