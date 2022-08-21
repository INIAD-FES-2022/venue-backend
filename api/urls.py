from django.urls import path, include
from . import apis
from rest_framework import routers

router = routers.DefaultRouter()
router.register('program', apis.ProgramViewSet)
router.register('notice', apis.NoticeViewSet)
router.register('group', apis.GroupViewSet)
router.register('category', apis.CategoryViewSet)
router.register('image', apis.ImageViewSet)
router.register('link', apis.LinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]