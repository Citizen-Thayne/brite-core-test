from rest_framework import serializers
from rest_framework.validators import ValidationError
from app.models import AbstractRiskFieldType, RiskType, DateRiskField, EnumRiskField, NumberRiskField, TextRiskField


class TextRiskFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextRiskField
        exclude = ('content_type', 'risk_type')


class NumberRiskFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberRiskField
        exclude = ('content_type', 'risk_type')


class EnumRiskFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnumRiskField
        exclude = ('content_type', 'risk_type')


class DateRiskFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateRiskField
        exclude = ('content_type', 'risk_type')


class RiskTypeFieldSerializer(serializers.Serializer):
    DATA_TYPE_SERIALIZERS = {
        TextRiskField: TextRiskFieldSerializer(),
        EnumRiskField: EnumRiskFieldSerializer(),
        DateRiskField: DateRiskFieldSerializer(),
        NumberRiskField: NumberRiskFieldSerializer()
    }
    DATA_TYPE_NAMES = {
        TextRiskField: 'text',
        EnumRiskField: 'enum',
        DateRiskField: 'date',
        NumberRiskField: 'number'
    }

    def to_representation(self, obj):
        risk_field = obj.as_leaf_class()
        serializer = self.DATA_TYPE_SERIALIZERS[risk_field.__class__]
        data = serializer.to_representation(risk_field)
        data['data_type'] = self.DATA_TYPE_NAMES[risk_field.__class__]
        return data


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = RiskTypeFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = ('id', 'name', 'fields')
        depth = 1
