from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse, resolve
from rest_api.models import Url


class PathsUrlsTestCase(APITestCase):

    def url_object_creation(self):
        """
        Testing that the post should create a new Url object
        """
        url = reverse('create_url')
        data = {"link": "somedummyurltotest.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Url.objects.count(), 1)
        self.assertEqual(Url.objects.get().link, 'somedummyurltotest.com')

    def two_request_different_url(self):
        """
        a second different request should create a new object
        """
        url = reverse('create_url')
        data = {"link": "test.com"}
        self.client.post(url, data, format='json')
        data = {"link": "testurlsecondrequestdifferent.com"}
        self.client.post(url, data, format='json')
        self.assertEqual(Url.objects.count(), 2)

    def second_request_same_url(self):
        """
        Testing if the request count is incremented after a second request to the same url
        """
        url = reverse('create_url')
        data = {"link": "test.com"}
        self.client.post(url, data, format='json')
        data = {"link": "test.com"}
        self.client.post(url, data, format='json')
        self.assertEqual(Url.objects.count(), 1)
        self.assertEqual(Url.objects.get().count_request, 2)
