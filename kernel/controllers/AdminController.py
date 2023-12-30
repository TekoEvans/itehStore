from models import Product, Subscriber
from tools.email import *
from app import updateConfigFile, data, db, createHash
from flask import render_template, request, redirect, session
import json

SOCIETY_FOLDER = '../static/img/society/'

class AdminController :

    def home():
        if session == {} :
            return redirect('/admin/login')
        return render_template('admin/pages/home.html', home=True, society=data)
    
    def society():
        if session == {} :
            return redirect('/admin/login')
        if(request.method == 'GET'):
            return render_template('admin/pages/society.html', main=True, society=data)
        for value in ['name','email','whatsapp','facebook','instagram','twitter','welcomeText','aboutText','map']:
            data[value] = request.form[value]
        for value in ['logo', 'header', 'contact', 'about'] :
            if(value in request.files):
                logo = request.files[value]
                if(logo.filename != ''):
                    logo.save(SOCIETY_FOLDER+ value +'.png')
        updateConfigFile(data)
        return render_template('admin/pages/society.html', main=True, society=data)
        
    # def notifySubscribers(id):
    #     if request.method == "POST":
    #         sendNewsletter(id)
    #     return redirect(request.url)

    def products():
        if session == {} :
            return redirect('/admin/login')
        searchText = None
        if(request.method == 'POST'):
            searchText = request.form['searchText']
            products = Product.query.filter(Product.name.like('%'+ searchText +'%')).all()
        else :
            products = Product.query.all()
        return render_template('admin/pages/products.html', product=True, society=data, articles=products, search_text=searchText)

    def login():
        if request.method == "GET":
            return render_template('admin/pages/login.html', society=data)
        name = request.form['name']
        password = createHash(request.form['password'])
        if data['username'] == name and data['password'] == password :
            session['admin'] = {
                "username" : name,
                "password" : password
            }
            return redirect('/admin')
        return render_template('admin/pages/login.html', society=data, error="Nom d'utilisateur ou mot de passe invalide.")

    def setting():
        if session == {} :
            return redirect('/admin/login')
        if request.method == "GET":
            return render_template('admin/pages/setting.html', society=data)
        old_username = request.form['old_username']
        old_password = createHash(request.form['old_password'])
        new_username = request.form['new_username']
        new_password = createHash(request.form['new_password'])
        new_password_confirmation = createHash(request.form['new_password_confirmation'])
        if data['username'] == old_username and data['password'] == old_password :
            if(new_password == new_password_confirmation):
                session['admin'] = {
                    "username" : new_username,
                    "password" : new_password
                }
                return redirect('/admin')
            else :
                error = "Nouveau mot de passe mal confirmé. Veillez réessayer."
        else :
            error = "Anciens identifiants invalides."
        data['old_username'] = old_username
        data['new_username'] = new_username
        return render_template('admin/pages/setting.html', society=data, error=error)

    def logout():
        if session != {} :
            session.pop('admin', None)
        return redirect('/admin/login')
