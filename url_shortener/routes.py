from flask import Blueprint
short = Blueprint('short', __name__, url_prefix='/shorten')
@short.route('/')
def index():
    return "Welcome to the shortening service"