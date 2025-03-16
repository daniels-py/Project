from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class listUserstest(TestCase):

    def test_should_return_200(self):
        url = reverse('list_users')
        response = self.client.get(url)
        breakpoint()
        self.assertEqual(response.status_code, 200)
   