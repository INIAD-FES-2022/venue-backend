from django.urls import path, include
from . import apis
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('program', apis.ProgramViewSet)
router.register('notice', apis.NoticeViewSet)
router.register('group', apis.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

