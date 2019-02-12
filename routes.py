from typing import Dict, Any
import os
from flask import Flask, render_template, request, app
from flask_sqlalchemy import SQLAlchemy

import psycopg2
#from flask_wtf import FlaskForm
#from wtforms_sqlalchemy.fields import QuerySelectField

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxxblesrascyio:a447ed84172575a035b9fa57af3f819f0c1163fe46da6c3469f110293e0412f1@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d37d890uhbs9gv'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class gs(db.Model):

    __tablename__= "GStable"

    id = db.Column(db.Integer, primary_key=True)
    subjectName = db.Column(db.String(100), unique=False)
    courseID = db.Column(db.String(100), unique=False)
    lecOrSection = db.Column(db.String(100), unique=False)
    enrollCode = db.Column(db.String(100), unique=False)
    days = db.Column(db.String(100), unique=False)
    times = db.Column(db.String(100), unique=False)
    locations = db.Column(db.String(100), unique=False)

    def __init__(self, subjectName, courseID, lecOrSection, enrollCode, days, times, locations):
        self.subjectName = subjectName
        self.courseID = courseID
        self.lecOrSection = lecOrSection
        self.enrollCode = enrollCode
        self.days = days
        self.times = times
        self.locations = locations


@app.route("/")
def index():
    datas = gs.query.all()
    courseData = db.session.query(gs).filter(gs.subjectName == "Anthropology").all()

    subject_set = set()
    couseID_set = set()
    for r in datas:
        subject_set.add(r.subjectName)



    return render_template('index.html', displayData=courseData)


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)