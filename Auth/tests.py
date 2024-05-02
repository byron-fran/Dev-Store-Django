from django.test import TestCase
from .models import User

# Create your tests here.

class UserTest(TestCase):
    
    def setUp(self) -> None:
        self.user = User.objects.create(username="jhon", email="jhon@gmail.com", password="jhon123")
        
    def test_create_user(self):
        
        self.assertEqual(self.user.username, 'jhon')    
        self.assertEqual(self.user.email,'jhon@gmail.com')
        self.assertFalse(self.user.check_password('jhon123'))
        
    def test_login_user(self):
        self.assertEqual(self.user.email, 'jhon@gmail.com')
        self.assertFalse(self.user.check_password('jhon123'))