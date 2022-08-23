from django_filters.rest_framework import DjangoFilterBackend
from .models import Program, Notice, Group, Category, Image, Link
from rest_framework import viewsets, filters
from .serializers import ProgramSerializer, NoticeSerializer, GroupSerializer, CategorySerializer, ImageSerializer, LinkSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'place', 'start_at', 'end_at', 'group']
    ordering_fields = ['start_at', 'end_at', 'title', 'group', 'category']
    ordering = ['title']

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category']
    ordering_fields = ['title', 'category', 'date']
    ordering = ['date']

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()