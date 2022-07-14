from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ConversionTestCase(TestCase):
    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Convert currencies using our app</h1>', html)

    def test_convert_form(self):
        with app.test_client() as client:
            res = client.post('/conversion', 
                            query_string = {'bcurr': 'USD',
                                            'tcurr': 'USD',
                                            'amt': '100.0'})
            
            self.assertIn(b'$ 100.0', res.data)
    
    def test_errs_in_form(self):
        with app.test_client() as client:
            res = client.post('/conversion', 
                            query_string = {'bcurr': 'asdf',
                                            'tcurr': 'UasfdD',
                                            'amt': '-55'})

            self.assertIn(b'Not a valid code: MUPPET', res.data)
