from flask import Blueprint,render_template
import os
from flask_one.extensions import mongo

main = Blueprint('main',__name__)

@main.route('/')
def index():
    todo_collection = mongo.db.todo
    todos = todo_collection.find()

    print("hallo {}".format(os.environ['FLASK_RUN_PORT']))
    return render_template('index.html',todos=todos)
