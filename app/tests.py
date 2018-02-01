import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from risk_types.models import RiskTypeField, RiskType


class RiskTypeTests(APITestCase):
    def test_create_risk_type(self):
        url = reverse('risktype-list')
        data = {
            'name': 'Automobile',
            'fields': [
                {
                    'name': 'Make',
                    'data_type': 't'
                },
                {
                    'name': 'Model',
                    'data_type': 't'
                 },
                {
                    'name': 'Year',
                    'data_type': 't'
                 },
                {
                    'name': 'Color',
                    'data_type': 'e'
                },
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RiskType.objects.count(), 1)
        self.assertEqual(RiskType.objects.get().name, 'Automobile')
        self.assertEqual(RiskType.objects.get().fields.count(), 4)

    def test_get_risk_type(self):
        prize_type = RiskType.objects.create(name='Prize')
        prize_amount_field = RiskTypeField.objects.create(name='Prize Amount', risk_type=prize_type, data_type='n')
        url = reverse('risktype-detail', kwargs={'pk': prize_amount_field.id})
        response = self.client.get(url, format='json')
        data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'Prize')
        self.assertEqual(data['fields'], [{'name': 'Prize Amount', 'data_type': 'n'}])

    def test_update_risk_type(self):
        prize_type = RiskType.objects.create(name='Prize')
        prize_amount_field = RiskTypeField.objects.create(name='Prize Amount', risk_type=prize_type, data_type='n')
        url = reverse('risktype-detail', kwargs={'pk': prize_amount_field.id})
        update = {'name': 'Game Prize'}
        response = self.client.patch(url, update, format='json')
        data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['name'], 'Game Prize')
        self.assertEqual(data['fields'], [{'name': 'Prize Amount', 'data_type': 'n'}])

    def test_delete_risk_type(self):
        prize_type = RiskType.objects.create(name='Prize')
        prize_amount_field = RiskTypeField.objects.create(name='Prize Amount', risk_type=prize_type, data_type='n')
        url = reverse('risktype-detail', kwargs={'pk': prize_amount_field.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RiskType.objects.count(), 0)


