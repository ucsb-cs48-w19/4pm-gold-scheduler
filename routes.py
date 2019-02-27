#<<<<<<< HEAD
#import os
#import json
#from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
#
#
#app = Flask(__name__)
#
## app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxxblesrascyio:a447ed84172575a035b9fa57af3f819f0c1163fe46da6c3469f110293e0412f1@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d37d890uhbs9gv'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#db = SQLAlchemy(app)
#
#class gs(db.Model):
#
#    __tablename__= "spring2019table"
#
#    id = db.Column(db.Integer, primary_key=True)
#    subjectName = db.Column(db.String(100), unique=False)
#    courseID = db.Column(db.String(100), unique=False)
#    lecOrSection = db.Column(db.String(100), unique=False)
#    proName = db.Column(db.String(100), unique=False)
#    enrollCode = db.Column(db.String(100), unique=False)
#    days = db.Column(db.String(100), unique=False)
#    times = db.Column(db.String(100), unique=False)
#    locations = db.Column(db.String(100), unique=False)
#
#    def __init__(self, subjectName, courseID, lecOrSection, proName, enrollCode, days, times, locations):
#        self.subjectName = subjectName
#        self.courseID = courseID
#        self.lecOrSection = lecOrSection
#        self.proName = proName
#        self.enrollCode = enrollCode
#        self.days = days
#        self.times = times
#        self.locations = locations
#
#
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#
#@app.route('/class-select')
#def dropDownPageNew():
#    datas = gs.query.all()
#    subject_set = set()
#    for r in datas:
#        subject_set.add(r.subjectName)
#
#    return render_template('dropDownPageNew.html', displayData=list(sorted(subject_set)))
#
#
#@app.route('/load_ajax', methods=["GET", "POST"])
#def load_ajax():
#    name = request.get_json()
#    returnData = db.session.query(gs).filter(gs.subjectName == name).all()
#
#    return_list = list()
#    for r in returnData:
#        return_list.append(r.courseID)
#
#    return_list = list(dict.fromkeys(return_list))
#
#    return json.dumps(return_list)
#
#
#@app.route('/load_ajax2', methods=["GET", "POST"])
#def load_ajax2():
#    courseName = request.get_json()
#
#    timesData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
#    proData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
#    lecDays = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
#
#    proData_list = list()
#
#    for r in proData:
#        proData_list.append(r.proName)
#
#    times_list = list()
#    for r in timesData:
#        times_list.append(r.times)
#
#    days_list = list()
#    for r in lecDays:
#        days_list.append(r.days)
#
#    return_list = list()
#    for r in range (0, len(proData_list)):
#        temp = proData_list[r] + "~" + days_list[r] + '~' + times_list[r]
#        return_list.append(temp)
#
#    return json.dumps(return_list)
#
#
#@app.route('/load_ajax3', methods=["GET", "POST"])
#def load_ajax3():
#    proAndTimes = request.get_json()
#    print(proAndTimes)
#    prof, day, time = proAndTimes.split('~')
#    returnData = db.session.query(gs).filter((gs.proName == prof) & (gs.times == time)).limit(1).all()
#
#    classId = returnData[0].id
#    classId += 1
#    print("classId: ", classId)
#
#    sectionTime_list = list()
#    sectionDay_list = list()
#    return_list = list()
#
#    sectionCheck = "0"
#    while sectionCheck == "0":
#        temp = db.session.query(gs).filter(gs.id == (classId)).limit(1).all()
#        sectionCheck = temp[0].lecOrSection
#        if (sectionCheck == "1") :
#             break
#        sectionTime_list.append(temp[0].times)
#        sectionDay_list.append(temp[0].days)
#        classId += 1
#
#    for r in range (0, len(sectionTime_list)):
#        temp = sectionDay_list[r] + "~" + sectionTime_list[r]
#        return_list.append(temp)
#
#    return json.dumps(return_list)
#
#
#if __name__ == "__main__":
#    db.create_all()
#    app.run(debug=True)
#=======
## import os
## import json
## from flask import Flask, render_template, request
## from flask_sqlalchemy import SQLAlchemy
##
##
## app = Flask(__name__)
##
## app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jxxblesrascyio:a447ed84172575a035b9fa57af3f819f0c1163fe46da6c3469f110293e0412f1@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d37d890uhbs9gv'
## #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
## app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##
## db = SQLAlchemy(app)
##
## class gs(db.Model):
##
##     __tablename__= "spring2019table"
##
##     id = db.Column(db.Integer, primary_key=True)
##     subjectName = db.Column(db.String(100), unique=False)
##     courseID = db.Column(db.String(100), unique=False)
##     lecOrSection = db.Column(db.String(100), unique=False)
##     proName = db.Column(db.String(100), unique=False)
##     enrollCode = db.Column(db.String(100), unique=False)
##     days = db.Column(db.String(100), unique=False)
##     times = db.Column(db.String(100), unique=False)
##     locations = db.Column(db.String(100), unique=False)
##
##     def __init__(self, subjectName, courseID, lecOrSection, proName, enrollCode, days, times, locations):
##         self.subjectName = subjectName
##         self.courseID = courseID
##         self.lecOrSection = lecOrSection
##         self.proName = proName
##         self.enrollCode = enrollCode
##         self.days = days
##         self.times = times
##         self.locations = locations
##
##
## @app.route('/')
## def index():
##     return render_template('index.html')
##
##
## @app.route('/class-select')
## def dropDownPageNew():
##     datas = gs.query.all()
##     subject_set = set()
##     for r in datas:
##         subject_set.add(r.subjectName)
##
##     return render_template('scheduleMaker.html', displayData=list(sorted(subject_set)))
##
##
## @app.route('/load_ajax', methods=["GET", "POST"])
## def load_ajax():
##     name = request.get_json()
##     returnData = db.session.query(gs).filter(gs.subjectName == name).all()
##
##     return_list = list()
##     for r in returnData:
##         return_list.append(r.courseID)
##
##     return_list = list(dict.fromkeys(return_list))
##
##     return json.dumps(return_list)
##
##
## @app.route('/load_ajax2', methods=["GET", "POST"])
## def load_ajax2():
##     courseName = request.get_json()
##
##     timesData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
##     proData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
##     lecDays = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
##
##     proData_list = list()
##
##     for r in proData:
##         proData_list.append(r.proName)
##
##     times_list = list()
##     for r in timesData:
##         times_list.append(r.times)
##
##     days_list = list()
##     for r in lecDays:
##         days_list.append(r.days)
##
##     return_list = list()
##     for r in range (0, len(proData_list)):
##         temp = proData_list[r] + "~" + days_list[r] + '~' + times_list[r]
##         return_list.append(temp)
##
##     return json.dumps(return_list)
##
##
## @app.route('/load_ajax3', methods=["GET", "POST"])
## def load_ajax3():
##     proAndTimes = request.get_json()
##     prof, day, time = proAndTimes.split('~')
##     returnData = db.session.query(gs).filter((gs.proName == prof) & (gs.times == time)).limit(1).all()
##
##     classId = returnData[0].id
##     classId += 1
##
##     sectionTime_list = list()
##     sectionDay_list = list()
##     return_list = list()
##
##     sectionCheck = "0"
##     while sectionCheck == "0":
##         temp = db.session.query(gs).filter(gs.id == (classId)).limit(1).all()
##         sectionCheck = temp[0].lecOrSection
##         if (sectionCheck == "1") :
##              break
##         sectionTime_list.append(temp[0].times)
##         sectionDay_list.append(temp[0].days)
##         classId += 1
##
##     for r in range (0, len(sectionTime_list)):
##         temp = sectionDay_list[r] + "~" + sectionTime_list[r]
##         return_list.append(temp)
##
##     return json.dumps(return_list)
##
##
## if __name__ == "__main__":
##     db.create_all()
##     app.run(debug=True)
#>>>>>>> df17829a8df8bdb9a5567dc1ef0042474c481f3a

