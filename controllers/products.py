import sqlalchemy
import sqlalchemy.orm

from flask import jsonify
from model.models import Product
import constants.responses as responses

def get_products(db, product_code=None):
    session: sqlalchemy.orm.Session = db.session

    try:
        if product_code:
            product_list = session.query(Product).filter(Product.productCode == product_code).all()
            error_message = "PRODUCT_NOT_FOUND"
        else:
            product_list = session.query(Product).order_by(Product.productCode).all()
            error_message = "PRODUCTS_NOT_FOUND"
    except Exception as e:
        session.rollback()        
        raise e
    finally:
        session.close()

    if product_list:
        return jsonify([product.to_json() for product in product_list])
    else: 
        return responses.not_found(error_message)



