from __init__ import db


class gs(db.Model):

    __tablename__= "spring2019table"

    id = db.Column(db.Integer, primary_key=True)
    subjectName = db.Column(db.String(100), unique=False)
    courseID = db.Column(db.String(100), unique=False)
    lecOrSection = db.Column(db.String(100), unique=False)
    proName = db.Column(db.String(100), unique=False)
    enrollCode = db.Column(db.String(100), unique=False)
    days = db.Column(db.String(100), unique=False)
    times = db.Column(db.String(100), unique=False)
    locations = db.Column(db.String(100), unique=False)

    def __init__(self, subjectName, courseID, lecOrSection, proName, enrollCode, days, times, locations):
        self.subjectName = subjectName
        self.courseID = courseID
        self.lecOrSection = lecOrSection
        self.proName = proName
        self.enrollCode = enrollCode
        self.days = days
        self.times = times
        self.locations = locations
