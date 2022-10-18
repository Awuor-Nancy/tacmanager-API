from django.urls import URLPattern, path, include
from api.models import Bills, Tax, Team
from rest_framework import routers
from .views import BillViewSet, TaxViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'Bills', BillViewSet,basename = Bills)
router.register(r'Tax', TaxViewSet, basename = Tax)
router.register(r'Team', TeamViewSet, basename= Team)

urlpatterns = [
    path('', include(router.urls)),
]



