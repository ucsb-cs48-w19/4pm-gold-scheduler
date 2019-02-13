from typing import Dict, Any
import os
import json
from flask import Flask, render_template, request, app, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxxblesrascyio:a447ed84172575a035b9fa57af3f819f0c1163fe46da6c3469f110293e0412f1@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d37d890uhbs9gv'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

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

# class Form(FlaskForm):
#     subject_name = SelectField('subject_name', choices=[('Anthropology', 'Anthropology'), ('Art', 'Art')])
#     course_id = SelectField('course_id', choices=[])
#
#
# @app.route("/", methods=["GET", "POST"])
# def calender():
#     form = Form()
#     form.subject_name.choices = [(course_id.id, course_id.name)for course_id in gs.query.filter_by(subject_name="Anthropology").all()]
#
#     return render_template('calendar.html', form=form)

@app.route("/", methods=["GET", "POST"])
def index():
    datas = gs.query.all()
    courseData = db.session.query(gs).filter(gs.subjectName == "Anthropology").all()

    subject_set = set()
    couseID_set = set()
    for r in datas:
       subject_set.add(r.subjectName)

    return render_template('index.html', displayData=courseData)

@app.route('/load_ajax', methods=["GET", "POST"])
def load_ajax():
    name = request.get_json()
    print(name)
    returnData = db.session.query(gs).filter(gs.subjectName == name).all()

    return_set = set()
    for r in returnData:
        return_set.add(r.courseID)
    print(sorted(return_set))

    return json.dumps(sorted(return_set))



@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/dropDownPageNew')
def dropDownPageNew():
    datas = gs.query.all()
    subject_set = set()
    for r in datas:
        subject_set.add(r.subjectName)

    return render_template('dropDownPageNew.html', displayData=list(sorted(subject_set)))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)