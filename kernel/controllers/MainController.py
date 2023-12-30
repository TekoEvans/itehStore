from flask import render_template, redirect, request
from app import db, data
from models import Product

class MainController :
    def home():
        products = Product.query.order_by(Product.created_at.desc()).limit(30)
        return render_template("app/pages/home.html", home=True, articles=products, society=data)

    # def send_email():
    #     if request.method == "POST":
    #         sendContactEmail({
    #             "sender_name" : request.form['name'],
    #             "sender_email" : request.form['email'],
    #             "sender_message": request.form['message']
    #         })
    #     return redirect(request.url)

    # def subscribe():
    #     if request.method == "POST":
    #         email = request.form['email']
    #         subscriber = Subscriber(email=email)
    #         try :
    #             db.session.add(subscriber)
    #             db.session.commit()
    #             sendWelcomeEmail(email)
    #         except Exception as ex :
    #             pass
    #     return redirect(request.url)

    # def unsubscribe(email):
    #     if request.method == "GET":
    #         subscriber = Subscriber.query.get_or_404(Subscriber.email == email)
    #         try :
    #             db.session.delete(subscriber)
    #             db.session.commit()
    #             sendByeEmail(email)
    #         except Exception as ex :
    #             pass
    #     return redirect(request.url)

    def contact():
        return render_template('app/pages/contact.html', contact=True, society=data)
    
    def about():
        return render_template('app/pages/about.html', about=True, society=data)
    

