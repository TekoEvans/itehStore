from flask_mail import Message
from app import *
from models import Product, Subscriber

def sendContactEmail(params):
    sender = params['sender_email']
    msg = Message("Nouveau message de contact.", sender=sender, recipients=[data['email']])
    msg.body = """
        <div class="body">
            <span class="align-center" style="margin-bottom: 12px;">
                <img class="logo" src="../../static/img/society/logo.png" alt="Logo" />
                <span class="society_name">{}</span>
            </span>
            <div class="">
                <p class="title" style="color: rgb(51 65 85);">Nouveau message de contact !</p>
                <div class="message-box">
                    <p class="name"><span class="from">De la part de</span> <br /><br />&nbsp;&nbsp;&nbsp;&nbsp;{},
                    </p>
                    <p class="message">&nbsp;&nbsp;&nbsp;&nbsp;{}</p>
                </div>
            </div>
            <div class="">
                <p class="">Copyright © 2022 - All rights reserved by {}</p>
            </div>
        </div>
        """.format(data['name'], params['sender_name'], params['sender_message'], data['name'])
    email.send(msg)
    # email.send(
    #     subject = "Nouveau message de contact.",
    #     receivers = [data['email']],
    #     # <style>* {font-family: Verdana, 'Times New Roman', Times, serif;}html {    height: 100%;}.align-center {    display: flex;    align-items: center;    justify-content: center;}.title {    width: max-content;    border-left: 12px solid rgb(51 65 85);    padding: 7px;    font-weight: bold;    font-size: large;    font-size: 1.875rem;    line-height: 2.25rem;}.body {    height: 100%;    display: flex;    flex-direction: column;    background: rgb(249 250 251);    align-items: center;    justify-content: center;}.logo {    height: 3rem;}.container {    width: 70%;    height: 70%;    margin-left: auto;    margin-right: auto;}.society_name {    font-size: 1.875rem;    line-height: 2.25rem;    margin-left: 12px;}.name {    font-weight: bold;    font-size: large;    font-size: 1.700rem;    line-height: 2.25rem;}.message-box {    padding-left: 55px;    padding-right: 55px;    margin-top: 4rem;    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.message {    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.from {    font-weight: lighter;    font-size: 1.700rem;    line-height: 2.25rem;}
    #     html = """
    #     <div class="body">
    #         <span class="align-center" style="margin-bottom: 12px;">
    #             <img class="logo" src="../../static/img/society/logo.png" alt="Logo" />
    #             <span class="society_name">{}</span>
    #         </span>
    #         <div class="">
    #             <p class="title" style="color: rgb(51 65 85);">Nouveau message de contact !</p>
    #             <div class="message-box">
    #                 <p class="name"><span class="from">De la part de</span> <br /><br />&nbsp;&nbsp;&nbsp;&nbsp;{},
    #                 </p>
    #                 <p class="message">&nbsp;&nbsp;&nbsp;&nbsp;{}</p>
    #             </div>
    #         </div>
    #         <div class="">
    #             <p class="">Copyright © 2022 - All rights reserved by {}</p>
    #         </div>
    #     </div>
    #     """.format(data['name'], params['sender_name'], params['sender_message'], data['name'])
    # )

def sendWelcomeEmail(email):
    app.config["EMAIL_SENDER"] = data['email']
    email.send(
        subject = "Inscription réussie chez " + data['name'] + " !",
        receivers = email,
        html = """
            <style>* {font-family: Verdana, 'Times New Roman', Times, serif;}html {    height: 100%;}.align-center {    display: flex;    align-items: center;    justify-content: center;}.title {    width: max-content;    border-left: 12px solid rgb(51 65 85);    padding: 7px;    font-weight: bold;    font-size: large;    font-size: 1.875rem;    line-height: 2.25rem;}.body {    height: 100%;    display: flex;    flex-direction: column;    align-items: center;    justify-content: center;}.logo {    height: 3rem;}.container {    width: 70%;    height: 70%;    margin-left: auto;    margin-right: auto;}.society_name {    font-size: 1.875rem;    line-height: 2.25rem;    margin-left: 12px;}.name {    font-weight: bold;    font-size: large;    font-size: 1.700rem;    line-height: 2.25rem;}.message-box {    padding-left: 55px;    padding-right: 55px;    margin-top: 4rem;    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.message {    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.from {    font-weight: lighter;    font-size: 1.700rem;    line-height: 2.25rem;}div a {    color: white;    padding: 10px;    box-shadow: inset;    border-radius: 15px;    text-decoration: none;    background-color: rgb(59 130 246);}</style>
            <div class="body">
                <span class="align-center" style="margin-bottom: 12px;">
                    <img class="logo" src="../../static/img/society/logo.png" alt="Logo" />
                    <span class="society_name">{}</span>
                </span>
                <div class="">
                    <p class="title" style="color: rgb(51 65 85);">Vous êtes le bienvenu chez nous.</p>
                    <div class="message-box">
                        <p class="name">
                            Vous êtes désormais abonné au service d'information en cas de parution de nouveaux articles.
                        </p>
                        <p class="message">
                            Dès qu'un nouveau produit sera disponible chez nous, vous en serez automatiquement notifié.
                            <br/><br/>
                            <a href="/">Aller sur le site</a>
                        </p>
                    </div>
                </div>
                <div class="">
                    <p class="">Copyright © 2022 - All rights reserved by {}</p>
                </div>
            </div>
        """.format(data['name'], data['name'])
    )

def sendByeEmail(email):
    app.config["EMAIL_SENDER"] = data['email']
    email.send(
        subject = "Désinscription réussie chez " + data['name'] + ".",
        receivers = email,
        html = """
            <style>* {font-family: Verdana, 'Times New Roman', Times, serif;}html {height: 100%;}.align-center {display: flex;align-items: center;    justify-content: center;}.title {    width: max-content;    border-left: 12px solid rgb(51 65 85);    padding: 7px;    font-weight: bold;    font-size: large;    font-size: 1.875rem;    line-height: 2.25rem;}.body {    height: 100%;    display: flex;    flex-direction: column;    align-items: center;    justify-content: center;}.logo {    height: 3rem;}.container {    width: 70%;    height: 70%;    margin-left: auto;    margin-right: auto;}.society_name {    font-size: 1.875rem;    line-height: 2.25rem;    margin-left: 12px;}.name {    font-weight: bold;    font-size: large;    font-size: 1.700rem;    line-height: 2.25rem;}.message-box {    padding-left: 55px;    padding-right: 55px;    margin-top: 4rem;    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.message {    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.from {    font-weight: lighter;    font-size: 1.700rem;    line-height: 2.25rem;}div a {    color: white;    padding: 10px;    box-shadow: inset;    border-radius: 15px;    text-decoration: none;    background-color: rgb(59 130 246);}</style>
            <div class="body">
                <a class="align-center" style="margin-bottom: 12px;">
                    <img class="logo" src="../../static/img/society/logo.png" alt="Logo" />
                    <span class="society_name">{}</span>
                </a>
                <div class="">
                    <p class="title" style="color: rgb(51 65 85);">Nous regrettons votre désabonnement</p>
                    <div class="message-box">
                        <p class="name">
                            Vous êtes désormais désabonné à notre service d'information en cas de parution de nouveaux articles.
                        </p>
                        <p class="message">
                            N'hesitez pas à revenir nous voir, ou à nous contacter.
                            <br/><br/>
                            <a href="/">Aller sur le site</a>
                            <a href="/">Contact</a>
                        </p>
                    </div>
                </div>
                <div class="">
                    <p class="">Copyright © 2022 - All rights reserved by {}</p>
                </div>
            </div>
        """.format(data['name'], data['name'])
    )

def sendNewsletter(id):
    article = Product.query.get_or_404(id)
    for subscriber in Subscriber.query.all():
        app.config["EMAIL_SENDER"] = data['email']
        email.send(
            subject = "Nouvel article disponible chez nous !",
            receivers = [subscriber.email],
            html = """
                <style>* {font-family: Verdana, 'Times New Roman', Times, serif;}html {height: 100%;}.align-center {display: flex;align-items: center;    justify-content: center;}.title {    width: max-content;    border-left: 12px solid rgb(51 65 85);    padding: 7px;    font-weight: bold;    font-size: large;    font-size: 1.875rem;    line-height: 2.25rem;}.body {    height: 100%;    display: flex;    flex-direction: column;    align-items: center;    justify-content: center;}.logo {    height: 3rem;}.container {    width: 70%;    height: 70%;    margin-left: auto;    margin-right: auto;}.society_name {    font-size: 1.875rem;    line-height: 2.25rem;    margin-left: 12px;}.name {    font-weight: bold;    font-size: large;    font-size: 1.700rem;    line-height: 2.25rem;}.message-box {    padding-left: 55px;    padding-right: 55px;    margin-top: 4rem;    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.message {    font-size: medium;    font-size: 1.700rem;    line-height: 2.25rem;}.from {    font-weight: lighter;    font-size: 1.700rem;    line-height: 2.25rem;}div a {    color: white;    padding: 10px;    box-shadow: inset;    border-radius: 15px;    text-decoration: none;    background-color: rgb(59 130 246);}</style>
                <div class="body">
                    <span class="align-center" style="margin-bottom: 12px;">
                        <img class="logo" src="../../static/img/society/logo.png" alt="Logo" />
                        <span class="society_name">{}</span>
                    </span>
                    <div class="">
                        <p class="title" style="color: rgb(51 65 85);">Nouvel artcile disponible !</p>
                        <div class="message-box">
                            <p class="name">
                                <span class="from">
                                    Il s'agit d'un(e)
                                </span> <br /><br />&nbsp;&nbsp;&nbsp;&nbsp;
                                {}
                                <span class="name" style="font-weight: lighter;">
                                    à {} FCFA
                                </span>
                            </p>
                            <div>
                                &nbsp;&nbsp;&nbsp;&nbsp;
                                <img style="width: 25rem; height : 35rem; border-radius: 15px; object-fit: contain;" alt="image IPhone13 pro"
                                src="../../static/img/products/{}/main.png" />
                            </div>
                            <p class="message">&nbsp;&nbsp;&nbsp;&nbsp;{}</p>
                                <a href="/product/{}">Voir l'article</a>
                                <a href="/unsubscribe/{}">Se désabonner</a>
                                <a href="/">Aller sur le site</a>
                        </div>
                    </div>
                    <div class="">
                        <p class="">Copyright © 2022 - All rights reserved by {}</p>
                    </div>
                </div>
            """.format(data['name'], article.name, article.getPrice(), article.id, article.description, article.id, subscriber.email, data['name'])
        )