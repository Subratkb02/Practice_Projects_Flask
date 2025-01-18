from flask import Blueprint
short = Blueprint('short', __name__, url_prefix='/shortener')
@short.route('/')
def index():
    return "Welcome to the shortening service"
