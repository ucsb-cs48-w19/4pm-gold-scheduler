#test_connection.py
import pytest
import unittest

from flask import render_template, Flask, request, jsonify, session, redirect, url_for, flash

from routes import app


#this test is for getting data from the front end and sending data to the front end
#also will test get correct data from the database
#integration test



class connectionTestCase(unittest.TestCase):


	#these functions will test get the type of course and return all coutse name under this type

	#test for the first tyoe of course we have

	#this is the test for the first course in the list
	def test_return_of_load_ajax1_1(self):
		tester = app.test_client(self)
		#curl --header"Content=Type: application/json;charset=UTF-8"--request POST --data "'Art'"
		#response = curl--header"Content=Type: application/json;charset=UTF-8"--request POST --data "'Art'"
		response = tester.post('/load_ajax', data = '"Anthropology"',  content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"ANTH 2"' in response.data)
		#self.assertEqual(b'["ART 1A", "ART 1C", "ART 7A", "ART 10", "ART 12", "ART 14", "ART 22", "ART 100", 
		#"ART 101", "ART CS 101", "ART 106PP", "ART 110", "ART CS 112", "ART 113", "ART 117", "ART 118", "ART 120EF", 
		#"ART 122CC", "ART 123", "ART 130", "ART 134", "ART 137", "ART 185LJ", "ART 192ES", "ART 192IA", "ART 196", "ART 199", 
		#"ART 199RA"]', response.data)

	#this is the test for the last course in the list
	def test_return_of_load_ajax1_2(self):
		tester = app.test_client(self)
		#curl --header"Content=Type: application/json;charset=UTF-8"--request POST --data "'Art'"
		#response = curl--header"Content=Type: application/json;charset=UTF-8"--request POST --data "'Art'"
		response = tester.post('/load_ajax', data = '"Anthropology"',  content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"ANTH 199RA"' in response.data)

	#test for the last type of course we have
	#this is the test for the first course in this list
	def test_return_of_load_ajax1_3(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax', data = '"Writing&Literature(CreativeStudies)"',  content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"W&L CS 20"' in response.data)

	#this is the test for the last course in this list
	def test_return_of_load_ajax1_4(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax', data = '"Writing&Literature(CreativeStudies)"',  content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"W&L CS 152FF"' in response.data)



	#these functions will test get the course name and return any other information 
	#for this course

	#this function will test the lecture time for the first class for first course
	# for first type
	def test_return_of_load_ajax2_1(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax2', data = '"ANTH 2"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"WALSH C~M W F~11:00am - 11:50am"' in response.data)		

	#this function will test the lecture time for the last class for first course for
	# first type
	def test_return_of_load_ajax2_2(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax2', data = '"ANTH 199RA"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"T B A~T B A~T B A"' in response.data)		


	#this function will test the lecture time for the first class for last course for
	# last type
	def test_return_of_load_ajax2_3(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax2', data = '"W&L CS 20"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"BAZERMAN C~M W~9:30 am - 10:45am"' in response.data)		

	#this function will test the lecture time for the last class for last course for
	# last type
	def test_return_of_load_ajax2_4(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax2', data = '"W&L CS 152FF"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"TERVALON J~F~11:00am - 1:50pm"' in response.data)		

	#this function will test the first section time for the first class of the first type
	# in whole class list
	def test_return_of_load_ajax3_1(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax3', data = '"ANTH 2~WALSH C~M W F~11:00am - 11:50am"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"F~2:00pm - 2:50pm"' in response.data)

	#this function will test the last section time for the last class of the first type in
	# the whole class list
	def test_return_of_load_ajax3_2(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax3', data = '"ANTH 199RA~T B A~T B A~T B A"', content_type = 'application/json;charset=UTF-8')
		self.assertEqual(b'[]' , response.data)


	#this function will test the first section time for the last class(which have a section
	# time) for the last type in the whole class list
	def test_return_of_load_ajax3_3(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax3', data = '"THTR 2C~ASI A~M W~11:00am - 12:15pm"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"M~9:00 am - 9:50 am"' in response.data)

	#this function will test the last section time for the last class(whicl have a section 
	# time) for the last type in the whole class list
	def test_return_of_load_ajax3_4(self):
		tester = app.test_client(self)
		response = tester.post('/load_ajax3', data = '"THTR 23D~SCHMEDAKE A J~T R~2:00pm - 4:50pm"', content_type = 'application/json;charset=UTF-8')
		self.assertTrue(b'"T R~2:00pm - 4:50pm"' in response.data)


if __name__ == '__main__':
	unittest.main()

