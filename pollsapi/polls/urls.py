from rest_framework import routers

from . import views
router = routers.DefaultRouter()
router.register(r'questions', views.PollViewSet, basename='polls')
router.register(r'votes', views.VoteViewSet, basename='votes')
urlpatterns = router.urls
