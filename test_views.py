import os 
import tempfile
import json
from flask import Flask, render_template, request
from views import index
from app import app

def test_index():
  assert index() == render_template('index.html')
