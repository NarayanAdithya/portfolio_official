from app import application,models
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,jsonify

@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html',title='About Me',pos='home',dist=24)

@application.route('/projects')
def projects():
    return render_template('projects.html',title='Projects',pos='projects',dist=20)

@application.route('/contacts',methods=['POST','GET'])
def contacts():
    if(request.method=='POST'):
        return redirect(url_for('home'))
    return render_template('contacts.html',title='Contact',pos='contacts')

@application.route('/techstack')
def techstack():
    return render_template('techstack.html',title='TechStack',pos='techstack')