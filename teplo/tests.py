from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from teplo.models import Order


class GetPageTest(TestCase):
    def setUp(self):
        """Action before test"""
        pass

    def test_home(self):
        """Test get home page"""
        path = reverse('teplo:home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'главная')
        self.assertTemplateUsed(response, 'teplo/index.html')

    def test_about(self):
        """Test get about page"""
        path = reverse('teplo:about')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'о нас')
        self.assertTemplateUsed(response, 'teplo/about.html')

    def test_service(self):
        """Test get service page"""
        path = reverse('teplo:service')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'услуги')
        self.assertTemplateUsed(response, 'teplo/service.html')

    def test_price(self):
        """Test get price page"""
        path = reverse('teplo:price')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['title'], 'цены')
        self.assertTemplateUsed(response, 'teplo/price.html')

    def tearDown(self):
        """Action after test"""
        pass


class FormTest(TestCase):
    def setUp(self):
        """Action before test"""
        self.data_order = {
            'name': 'Юлий',
            'phone': "89998889988",
            'order': 'Требуется автоматизировать ИТП',
            'captcha': 'PASSED'
        }

    def test_form(self):
        path = reverse('teplo:home')
        response = self.client.post(path, data=self.data_order)  # fill form to send

        # self.assertEqual(response.status_code, HTTPStatus.FOUND)  # check redirection - code 302
        # self.assertRedirects(response, reverse('teplo:home'))  # check redirection target (home)
        # self.assertTrue(Order.objects.filter(name=self.data_order['name']).exists())  # check data in db

    def tearDown(self):
        """Action after test"""
        pass
