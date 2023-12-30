from flask import render_template, redirect, request
from sqlalchemy.sql.expression import func
from app import db, data
from tools.email import sendNewsletter
from models import Product
from datetime import datetime
import os, shutil,json

PRODUCT_FOLDER = 'static/img/products/'

SHORT_PRODUCT_FOLDER = 'img/products/'

class ProductController :
    def index():
        if(request.method == 'POST'):
            return redirect('/products/search=' + request.form['searchText'])
        products = Product.query.order_by(Product.name)
        return render_template('app/pages/products.html', product=True, articles=products, society=data)

    def products_search(text):
        products = Product.query.filter(Product.name.like('%'+ text +'%')).all()
        return render_template('app/pages/products.html', product=True, society=data, articles=products, search_text=text)
    
    def show(id):
        product = Product.query.get_or_404(id)
        products = Product.query.filter(Product.id != product.id).order_by(func.random())
        return render_template('app/pages/product.html', product=product, articles=products, society=data)

    def store():
        if(request.method == 'POST'):
            name = request.form['name']
            price = request.form['price']
            description = request.form['description']
            created_at = datetime.utcnow()
            updated_at = datetime.utcnow()
            product = Product(name=name, price=price, description=description, created_at=created_at, updated_at=updated_at)
            try :
                db.session.add(product)
                db.session.commit()
                product = Product.query.order_by(Product.id.desc()).first()
                images = json.loads(product.images)
                os.mkdir(PRODUCT_FOLDER + str(product.id))
                for value in ["main","one","two","three","four","five","six"]:
                    if(value in request.files):
                        file = request.files[value]
                        if(file.filename != ''):
                            file.save(PRODUCT_FOLDER + str(product.id) + '/'+ value +'.png')
                            images[value] = SHORT_PRODUCT_FOLDER + str(product.id) + '/'+ value +'.png'
                        product.images = json.dumps(images)
                        db.session.commit()
                return redirect('/admin/products')
            except Exception as ex:
                return render_template('admin/pages/products.html', product=True, error=ex, society=data)
        return redirect('/admin/products')
    
    def delete(id):
        product = Product.query.get_or_404(id)
        try :
            db.session.delete(product)
            db.session.commit()
            try :
                shutil.rmtree(PRODUCT_FOLDER + str(product.id))
            except Exception :
                pass
            return redirect('/admin/products')
        except Exception as ex :
            return render_template('admin/pages/products.html', product=product, error=ex, society=data)
    
    def update(id):
        if(request.method == 'POST'):
            product = Product.query.get_or_404(id)
            product.name = request.form['name']
            product.price = request.form['price']
            product.description = request.form['description']
            product.updated_at = datetime.utcnow()
            try :
                db.session.commit()
                images = json.loads(product.images)
                try :
                    os.mkdir(PRODUCT_FOLDER + str(product.id))
                except Exception :
                    pass
                for value in ["main","one","two","three","four","five","six"]:
                    if(value in request.files):
                        file = request.files[value]
                        if(file.filename != ''):
                            file.save(PRODUCT_FOLDER + str(product.id) + '/'+ value +'.png')
                            images[value] = SHORT_PRODUCT_FOLDER + str(product.id) + '/'+ value +'.png'
                        product.images = json.dumps(images)
                        db.session.commit()
                return redirect('/admin/products')
            except Exception as ex:
                return render_template('admin/pages/products.html', product=True, error=ex, society=data)
        return redirect('/admin/products')

