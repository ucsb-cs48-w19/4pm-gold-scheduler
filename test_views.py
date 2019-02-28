import pytest
import unittest

from flask import render_template, Flask, request, jsonify, session, redirect, url_for, flash
from views import index, dropDownPageNew
from app import app

# ensure that flask was set up the index page correctly
def test_views_index():
	tester = app.test_client()
	response = tester.get('/', content_type = 'html/text')
	assert response.status_code == 200


#ensure that flask was set up the course selection page correctly
def test_views_dropDownPageNew():
	tester = app.test_client()
	response = tester.get('/class-select', content_type = 'html/text')
	assert response.status_code == 200

