import os
import tempfile
import pytest

from routes import db, gs
#from routes import gs


#these functions will test wherther the gs class get the correct data from the database

def test_db():
	assert gs.__tablename__ == "spring2019table"

def test_init_1():
	if(gs.id == 1):
		assert gs.subjectName == "Anthropology"

def test_init_2():
	if(gs.id == 1):
		assert gs.courseID == "ANTH 2"

def test_init_3():
	if(gs.id == 1):
		assert gs.lecOrSection == "1"

def test_init_4():
	if(gs.id == 1):
		assert gs.proName == "WALSH C"

def test_init_5():
	if(gs.id == 1):
		assert gs.enrollCode == ""

def test_init_6():
	if(gs.id == 1):
		assert gs.days == "M W F"

def test_init_7():
	if(gs.id == 1):
		assert gs.times == "11:00am - 11:50am"

def test_init_8():
	if(gs.id == 1):
		assert gs.locations == "IV THEA1"


def test_init_9():
	if(gs.id == 4024):
		assert gs.subjectName == "Writing&Literature(CreativeStudies)"

def test_init_10():
	if(gs.id == 4024):
		assert gs.courseID == "W&L CS 152FF"

def test_init_11():
	if(gs.id == 4024):
		assert gs.lecOrSection == "1"

def test_init_12():
	if(gs.id == 4024):
		assert gs.proName == "T B A"

def test_init_13():
	if(gs.id == 4024):
		assert gs.enrollCode == ""

def test_init_14():
	if(gs.id == 4024):
		assert gs.days == "F"

def test_init_15():
	if(gs.id == 4024):
		assert gs.times == "11:00am - 1:50pm"

def test_init_16():
	if(gs.id == 4024):
		assert gs.locations == "CRST 143"
#	gs.__init__(gs,"Computer Science","1234567","CMPSC 8","Diba","lec","T W","11:00-12:15","Phelps")
#
#	assert gs.subjectName == "Course1"
#	assert gs.courseID == "1234567"
#	assert gs.lecOrSection == "lec"
#	assert gs.proName == "Bill"
#	assert gs.enrollCode == "123"
#	assert gs.days == "T"
#	assert gs.times == "11:00"
#	assert gs.locations == "Phelps"