from app import get_data
from app import app
from unittest import TestCase
from flask_debugtoolbar import DebugToolbarExtension
from flask import request



class FlaskAppTest(TestCase):
    def setUp(self):
        """before test setup"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_get_data(self):
        """Testing the correct values"""
        resp = self.client.post('/result', data = {'old': 'USD', 'to': 'EUR', 'amount': 2000})
        self.assertEqual(resp.status_code, 200)

        """Testing with invalid values"""
        resp = self.client.post('/result', data = {'old': 'AAA', 'to': 'ZZZ', 'amount': 400})
        self.assertEqual(resp.status_code, 302)