from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
urlpatterns = router.urls