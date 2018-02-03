import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import RiskType, EnumRiskField, NumberRiskField, TextRiskField, DateRiskField


class RiskTypeTests(APITestCase):
    def test_get_risk_type(self):
        prize_type = RiskType.objects.create(name='Prize')
        NumberRiskField.objects.create(name='Prize Amount', min_value=0.01, max_value=1000000.00, risk_type=prize_type)
        TextRiskField.objects.create(name='Prize Winner Name', min_length=2, max_length=100, risk_type=prize_type)

        url = reverse('risktype-detail', kwargs={'pk': prize_type.id})
        response = self.client.get(url, format='json')
        data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'Prize')
        self.assertDictEqual(data['fields'][0], {'id': 1, 'name': 'Prize Amount', 'dataType': 'number', 'minValue': 0.01, 'maxValue': 1000000.00})
        self.assertDictEqual(data['fields'][1], {'id': 2, 'name': 'Prize Winner Name', 'dataType': 'text', 'minLength': 2, 'maxLength': 100})
    def test_get_risk_type_list(self):
      automobile = RiskType.objects.create(name='Automobile')
      house = RiskType.objects.create(name='House')

      url = reverse('risktype-list')
      response = self.client.get(url, format='json')
      data = json.loads(response.content)

      self.assertEqual(len(data), 2)
      self.assertDictEqual(data[0], {'id': 1, 'name': 'Automobile', 'fields': []})
      self.assertDictEqual(data[1], {'id': 2, 'name': 'House', 'fields': []})

