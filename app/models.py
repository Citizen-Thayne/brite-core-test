from __future__ import unicode_literals

from django.db import models


class RiskType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class RiskTypeField(models.Model):
    DATA_TYPES = (
        ('t', 'Text'),
        ('n', 'Number'),
        ('d', 'Date'),
        ('e', 'Enum')
    )
    name = models.CharField(max_length=30)
    risk_type = models.ForeignKey(
        RiskType,
        related_name='fields',
        on_delete=models.CASCADE
    )
    data_type = models.CharField(
        max_length=1,
        choices=DATA_TYPES
    )

    def __str__(self):
        return f'{self.risk_type.name} > {self.name}'
