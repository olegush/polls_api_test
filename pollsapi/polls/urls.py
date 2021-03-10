from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register(r'questions', views.PollViewSet)
router.register(r'votes', views.VoteViewSet)
urlpatterns = router.urls
