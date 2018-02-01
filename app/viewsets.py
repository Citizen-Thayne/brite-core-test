from rest_framework import viewsets
from app.serializers import RiskTypeSerializer
from app.models import RiskType

class RiskTypeViewSet(viewsets.ModelViewSet):
  queryset = RiskType.objects.all()
  serializer_class = RiskTypeSerializer
