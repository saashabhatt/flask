from app import app
from unittest import TestCase
from models import db, connect_db, User, Post

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ConversionTestCase(TestCase):
    def test_home(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_user_id(self):
        with app.test_client() as client:
            res = client.get('/users/2')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>Ronnie Calculator</h2>', html)

    def test_add(self):
        with app.test_client() as client:
            res = client.post('/users/new', follow_redirects=True, data = {'fname': 'Barbara',
                                                                        'lname': 'Lighthouse',
                                                                        'img_url': 'http://tinyurl.com/missing-tv' })
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Barbara Lighthouse', res.data)
            
    def test_delete(self):
        with app.test_client() as client:
            user = User.query.filter_by(first_name="Barbara").first()
            res = client.post(f"/users/{user.id}/delete", follow_redirects=True)

            self.assertEqual(res.status_code, 200)

    def test_add_post(self):
        with app.test_client() as client:
            user = User.query.filter_by(first_name="Gary").first()
            res = client.post(f"/users/{user.id}/posts/new", follow_redirects=True, data = {'title': 'Clean the floor',
                                                                                            'content': 'How to videos',
                                                                                            'user_id': user.id})
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'Clean the floor', res.data)
    
    def test_delete_post(self):
        with app.test_client() as client:
            post = Post.query.filter_by(title="Clean the floor").first()
            res = client.post(f"/posts/{post.id}/delete", follow_redirects=True)

            self.assertEqual(res.status_code, 200)
            
