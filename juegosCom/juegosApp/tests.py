from django.test import TestCase
from django.urls import reverse
from perfiles.models import User


#PRUEBA CREAR JUEGO
class CrearJuegoTestCase(TestCase):
    def setUp(self):
        self.username = 'testusuario'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_crear_juego(self):
        self.client.login(username=self.username, password=self.password)

        url = reverse('crear_juego') 
        data = {
            'nombre': 'GTA',
            'descripcion': 'Descripcion',
            'genero': 'Accion Disparos',
            'lanzamiento': '2013-09-17',
            'clasificacion': 'A',
            'costo': 2000
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

#PRUEBA CREAR JUEGO GARTIS
class CrearJuegoGratisTestCase(TestCase):
    def setUp(self):
        self.username = 'testusuario'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_crear_juego_gratis(self):
        self.client.login(username=self.username, password=self.password)

        url = reverse('crear_juego_gratis') 
        data = {
            'nombre': 'GTA III',
            'descripcion': 'Descripcion',
            'genero': 'Accion Disparos',
            'lanzamiento': '2013-09-17',
            'clasificacion': 'A',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
