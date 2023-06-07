from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

#PRUEBA REGISTRO
class RegistroTestCase(TestCase):
    def test_registro(self):
        url = reverse('registro')
        data = {
            'username': 'testusuario',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('inicio'))  
        self.assertTrue(User.objects.filter(username='testusuario').exists())

#PRUEBA LOGIN
class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testusuario'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        url = reverse('login')
        login_data = {
            'username': self.username,
            'password': self.password
        }

        response = self.client.post(url, login_data)

        self.assertEqual(response.status_code, 302)  
        self.assertTrue(response.wsgi_request.user.is_authenticated) 

