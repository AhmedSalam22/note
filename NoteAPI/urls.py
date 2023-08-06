from django.urls import path, include
from rest_framework.routers import DefaultRouter
from NoteAPI.views import NoteViewSet, HomePage

router = DefaultRouter()
router.register('note', NoteViewSet)
urlpatterns = router.urls

# urlpatterns += [
#     path('', HomePage.as_view() )
# ]