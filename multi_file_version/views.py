# from flask import render_template, request
# from __init__ import db
# from app import app
# from models import gs
# import json
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/class-select')
# def scheduleMaker():
#     datas = gs.query.all()
#     subject_set = set()
#     for r in datas:
#         subject_set.add(r.subjectName)
#
#     return render_template('scheduleMaker.html', displayData=list(sorted(subject_set)))
#
#
# @app.route('/load_ajax', methods=["GET", "POST"])
# def load_ajax():
#     name = request.get_json()
#     returnData = db.session.query(gs).filter(gs.subjectName == name).all()
#
#     return_list = list()
#     for r in returnData:
#         return_list.append(r.courseID)
#
#     return_list = list(dict.fromkeys(return_list))
#
#     return json.dumps(return_list)
#
#
# @app.route('/load_ajax2', methods=["GET", "POST"])
# def load_ajax2():
#     courseName = request.get_json()
#     print("courseName: ",courseName)
#     timesData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
#     print("timesData: ", timesData)
#     proData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
#     print("proData: ", proData)
#     lecDays = db.session.query(gs).filter((gs.courseID == courseName) & (gs.lecOrSection == "1")).all()
#     print("lecDays:", lecDays)
#
#     proData_list = list()
#
#     for r in proData:
#         proData_list.append(r.proName)
#     print("prodata_list: ", proData_list)
#
#     times_list = list()
#     for r in timesData:
#         times_list.append(r.times)
#     print("times_list: ", times_list)
#
#     days_list = list()
#     for r in lecDays:
#         days_list.append(r.days)
#     print("days_list: ", days_list)
#
#     return_list = list()
#     for r in range(0, len(proData_list)):
#         temp = proData_list[r] + "~" + days_list[r] + '~' + times_list[r]
#
#         return_list.append(temp)
#
#     return json.dumps(return_list)
#
#
# @app.route('/load_ajax3', methods=["GET", "POST"])
# def load_ajax3():
#     proAndTimes = request.get_json()
#     courseName, prof, day, time = proAndTimes.split('~')
#     returnData = db.session.query(gs).filter((gs.courseID == courseName) & (gs.proName == prof) & (gs.times == time)).limit(1).all()
#
#     classId = returnData[0].id
#     classId += 1
#
#     sectionTime_list = list()
#     sectionDay_list = list()
#     return_list = list()
#
#     sectionCheck = "0"
#     while sectionCheck == "0":
#         temp = db.session.query(gs).filter(gs.id == classId).limit(1).all()
#         sectionCheck = temp[0].lecOrSection
#         if sectionCheck == "1":
#             break
#         sectionTime_list.append(temp[0].times)
#         sectionDay_list.append(temp[0].days)
#         classId += 1
#
#     for r in range(0, len(sectionTime_list)):
#         temp = sectionDay_list[r] + "~" + sectionTime_list[r]
#         return_list.append(temp)
#
#     return json.dumps(return_list)
