from flask import Blueprint

healthcheck_blueprint = Blueprint('index_blueprint', __name__)

@healthcheck_blueprint.route("/ping")
def healthCheck(): 
    return "pong"