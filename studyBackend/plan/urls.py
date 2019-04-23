from studyBackend.urls import router
from .views import PlanViewSets
router.register(r'plan', PlanViewSets)