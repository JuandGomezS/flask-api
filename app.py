from flask import Flask
from config.config import apiVersion, get_string_connection
from model.models import db
from routers.healthcheck import healthcheck_blueprint
from routers.products import products_blueprint



app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = get_string_connection()


db.init_app(app)

#healthChek
app.register_blueprint(healthcheck_blueprint)

#products router
app.register_blueprint(products_blueprint, url_prefix=apiVersion)

app.run(debug=True)