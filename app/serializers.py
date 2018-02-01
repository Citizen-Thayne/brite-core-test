from rest_framework import serializers
from app.models import RiskTypeField, RiskType


class RiskTypeFieldSerializer(serializers.ModelSerializer):
    data_type = serializers.ChoiceField(RiskTypeField.DATA_TYPES)

    class Meta:
        model = RiskTypeField
        fields = ('name', 'data_type')


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = RiskTypeFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = ('name', 'fields', 'url', 'id')
        depth = 1

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        risk_type = RiskType.objects.create(**validated_data)

        for field in fields_data:
            field = RiskTypeField(**field)
            field.risk_type = risk_type
            field.save()
        return risk_type
