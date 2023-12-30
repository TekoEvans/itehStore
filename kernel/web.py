 
from flask import Flask, render_template, request, redirect
from app import app, db
from controllers.AdminController import AdminController
from controllers.ProductController import ProductController
from controllers.MainController import MainController


# MainController functions

@app.route('/')
def index():
    return MainController.home()

@app.route('/about-us')
def about():
    return MainController.about()

# @app.route('/contact-us')
# def contact():
#     return MainController.contact()

# @app.route('/send-email', methods=['POST'])
# def send_email():
#     return MainController.send_email()

# @app.route('/unsubscribe/<string:email>', methods=['GET'])
# def unsubscribe(email):
#     return MainController.unsubscribe(email)

# @app.route('/subscribe', methods=['POST'])
# def subscribe():
#     return MainController.subscribe()


#ProductController functions

@app.route('/products', methods=['GET', 'POST'])
def products():
    return ProductController.index()

@app.route('/products/search=<string:text>', methods=['GET'])
def products_search(text):
    return ProductController.products_search(text=text)

@app.route('/product/<int:id>')
def product(id):
    return ProductController.show(id=id)

@app.route('/admin/product/store/', methods=['POST'])
def storeProduct():
    return ProductController.store()

@app.route('/admin/product/update/<int:id>', methods=['POST'])
def updateProduct(id):
    return ProductController.update(id=id)

@app.route('/admin/product/delete/<int:id>', methods=['GET'])
def deleteProduct(id):
    return ProductController.delete(id=id)

#AdminController functions

@app.route('/admin')
def admin_home():
    return AdminController.home()

@app.route('/admin/society', methods=['POST', 'GET'])
def admin_society():
    return AdminController.society()

@app.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    return AdminController.login()

@app.route('/admin/setting', methods=['POST', 'GET'])
def admin_setting():
    return AdminController.setting()

@app.route('/admin/logout', methods=['POST'])
def admin_logout():
    return AdminController.logout()

@app.route('/admin/products', methods=['GET', 'POST'])
def admin_products():
    return AdminController.products()

# @app.route('/admin/notifySubscribers/<int:id>', methods=['GET'])
# def admin_notifySubscribers(id):
#     return AdminController.notifySubscribers(id)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)