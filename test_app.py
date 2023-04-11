from app import get_data
from app import app
from unittest import TestCase
from flask_debugtoolbar import DebugToolbarExtension



class FlaskAppTest(TestCase):
    def setUp(self):
        """before test setup"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home():
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_get_data():
        