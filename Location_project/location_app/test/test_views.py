# tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from location_app.models import PlacesModel


class SignInTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.username = "Akhil"
        self.password = "1234"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.location1 = PlacesModel.objects.create(
            user_name=self.user,
            place_name="Peenya",
            description="Factory industry",
            latitude=12.345,
            longitude=67.890,
        )

    def test_valid_sign_in(self):
        # Create a client to simulate HTTP requests
        client = Client()

        # Perform a POST request to sign in with valid credentials
        response = client.post(
            "/sign-in/", {"username": self.username, "password": self.password}
        )

        # Check if the response is successful
        self.assertRedirects(response, "/index/", status_code=302)

    def test_invalid_sign_in(self):
        # Create a client to simulate HTTP requests
        client = Client()

        # Perform a POST request to sign in with invalid credentials
        response = client.post(
            "/sign-in/", {"username": "invaliduser", "password": "invalidpassword"}
        )

        # Check if the response indicates invalid credentials
        self.assertEqual(response.status_code, 200)

    def test_get_request(self):
        # Create a client to simulate HTTP requests
        client = Client()

        # Perform a GET request to the sign-in view
        response = client.get("/sign-in/")

        # Check if the response is a message to use the sign-in form
        self.assertEqual(response.status_code, 200)

    # def test_search(self):
    #     # Create a client to simulate HTTP requests
    #     client = Client()

    #     # Perform a POST request to sign in with invalid credentials
    #     response = client.post('/search/', {'user': 7, 'search_data': 'A'})
    #     print("\n\n\n response SEARCH",response," \n\n\n\n" )
    #     # Check if the response indicates invalid credentials
    #     self.assertEqual(response.status_code, 302)

    def test_search_data_found(self):
        # Test if the search_data function returns data for a valid search term
        client = Client()
        response = client.post("/search/", {"search_data": "a"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Peenya", response.content)
