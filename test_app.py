from app import get_data
from app import app



def test_get_data(self):
    with app.test_client() as client:

        resp = client.post('/result', daa= {'old': 'USD', 'to': 'GBR', 'amount': 5000})
        html = resp.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)