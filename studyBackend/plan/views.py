from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .serializers import PlanSerializer
from .models import Plan

# Create your views here.
class PlanViewSets(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
