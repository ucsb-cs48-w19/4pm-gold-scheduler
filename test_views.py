import os 
import tempfile
from flask import render_template
from views import index
from app improt app

def test_index():
  assert index() == render_template('index.html')
