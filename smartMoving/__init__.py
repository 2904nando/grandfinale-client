from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cajhzihnzlfeam:07cf65d371098ef1233562cddb5dfbe441010eec69a7677b4c1e8094c41e32b4@ec2-174-129-253-27.compute-1.amazonaws.com:5432/d1trbv2hk2ltgd'

    db = SQLAlchemy(app)

    from smartMoving import routes

    return app