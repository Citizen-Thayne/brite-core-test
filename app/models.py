from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet


class RiskType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubclassingQuerySet(QuerySet):
    def __getitem__(self, k):
        result = super(SubclassingQuerySet, self).__getitem__(k)
        if isinstance(result, models.Model):
            return result.as_leaf_class()
        else:
            return result

    def __iter__(self):
        for item in super(SubclassingQuerySet, self).__iter__():
            yield item.as_leaf_class()


class RisTypeFieldManager(models.Manager):
    def get_query_set(self):
        return SubclassingQuerySet(self.model)


class AbstractRiskFieldType(models.Model):
    name = models.CharField(max_length=30)
    content_type = models.ForeignKey(ContentType, editable=False, null=True, on_delete=models.DO_NOTHING)
    risk_type = models.ForeignKey(
        RiskType, on_delete=models.CASCADE, related_name='fields')
    objects = RisTypeFieldManager()


    def save(self, *args, **kwargs):
        if(not self.content_type):
            self.content_type = ContentType.objects.get_for_model(
                self.__class__)
            super(AbstractRiskFieldType, self).save(*args, **kwargs)

    def as_leaf_class(self):
        content_type = self.content_type
        model = content_type.model_class()
        if (model == AbstractRiskFieldType):
            return self
        return model.objects.get(id=self.id)


class TextRiskField(AbstractRiskFieldType):
    min_length = models.IntegerField(null=True)
    max_length = models.IntegerField(null=True)
    objects = RisTypeFieldManager()

    def validate(self, value):
        if self.minLength is not None and self.minLength > len(value):
            return False
        elif self.maxLength is not None and self.maxLength < len(value):
            return False
        else:
            return True


class NumberRiskField(AbstractRiskFieldType):
    min_value = models.FloatField(null=True)
    max_value = models.FloatField(null=True)
    objects = RisTypeFieldManager()

    def validate(self, value):
        if self.minLength is not None and self.minLength > value:
            return False
        elif self.maxLength is not None and self.maxLength < value:
            return False
        else:
            return True


class EnumRiskField(AbstractRiskFieldType):
    values = models.TextField()
    objects = RisTypeFieldManager()

    def validate(self, value):
        values = self.values.split(',')
        return value in values


class DateRiskField(AbstractRiskFieldType):
    min_date = models.DateField(null=True)
    max_date = models.DateField(null=True)
    objects = RisTypeFieldManager()

    def validate(self, value):
        if self.minDate is not None and self.minDate > value:
            return False
        elif self.maxDate is not None and self.maxDate < value:
            return False
        else:
            return True
