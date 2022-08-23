from django.urls import path, include
from . import apis
from django.conf import settings
from django.contrib.staticfiles.urls import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('program', apis.ProgramViewSet)
router.register('notice', apis.NoticeViewSet)
router.register('group', apis.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
