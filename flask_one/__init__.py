from flask import Flask
from .main.routes import main
from .extensions import mongo
import os

app = Flask(__name__)
app.register_blueprint(main)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo.init_app(app)
if __name__=='__main__':
    app.run()
