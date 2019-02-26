import os
import tempfile

import pytest

from __init__ import db

from models import gs


def test_db():
	assert gs.__tablename__ == "spring2019table"