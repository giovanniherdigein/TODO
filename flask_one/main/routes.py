from flask import Blueprint
import os
main = Blueprint('main',__name__)

@main.route('/')
def index():
    print("hallo {}".format(os.environ['FLASK_RUN_PORT']))
    return "Index"
