from app import get_data



def test_get_data(self):
    with app.test_client() as client:

        resp = client.get('/result')
        html = resp.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)