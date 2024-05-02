
from flask import Blueprint, request
from model.models import db
from controllers.products import get_products

products_blueprint = Blueprint("product_blueprint", __name__)


@products_blueprint.route("/products", methods=["GET", "POST"])
def products():
    if request.method == 'GET':
        product_code = request.args.get('product_code') 
        return get_products(db, product_code)
    else:
        return "Va por post"
