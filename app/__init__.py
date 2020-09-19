from flask import Flask,render_template,request,redirect,url_for,send_from_directory
from firebase_admin import credentials
from werkzeug.utils import secure_filename
from unicodedata import normalize
from firebase import firebase
from google.cloud import storage 
#from os import listdir
from os.path import isfile, isdir, join

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY']='superpasswordsuperpassword'
    
    from app.main.main import main
    
    app.register_blueprint(main)

    return app