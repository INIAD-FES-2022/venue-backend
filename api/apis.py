from django_filters.rest_framework import DjangoFilterBackend
from .models import Program, Notice, Group
from rest_framework import viewsets, filters
from .serializers import ProgramSerializer, DetailProgramSerializer, NoticeSerializer, DetailNoticeSerializer, GroupSerializer, DetailGroupSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    http_method_names = ["get"]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'place', 'start_at', 'end_at', 'group']
    ordering_fields = ['start_at', 'end_at', 'title', 'group', 'category']
    ordering = ['title']
    def get_serializer_class(self, *args, **kwargs):
        if self.action!='list':
            return DetailProgramSerializer
        else:
            return self.serializer_class

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    http_method_names = ["get"]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    ordering_fields = ['title', 'category', 'date']
    ordering = ['date']
    def get_serializer_class(self, *args, **kwargs):
        if self.action!='list':
            return DetailNoticeSerializer
        else:
            return self.serializer_class

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    http_method_names = ["get"]
    def get_serializer_class(self, *args, **kwargs):
        if self.action!='list':
            return DetailGroupSerializer
        else:
            return self.serializer_class
