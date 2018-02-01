from rest_framework import routers
from app.viewsets import RiskTypeViewSet

router = routers.DefaultRouter()
router.register(r'risktypes', RiskTypeViewSet)
