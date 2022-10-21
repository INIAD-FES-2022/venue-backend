from django_filters.rest_framework import DjangoFilterBackend
from .models import Program, Notice, Group
from rest_framework import viewsets, filters
from .serializers import ProgramSerializer, DetailProgramSerializer, NoticeSerializer, DetailNoticeSerializer, GroupSerializer, DetailGroupSerializer
from django.db.models import Case, When

class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    http_method_names = ["get"]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'place', 'start_at', 'end_at', 'group', 'is_online', 'is_face2face']
    ordering_fields = ['start_at', 'end_at', 'title', 'group']
    def get_serializer_class(self, *args, **kwargs):
        if self.action!='list':
            return DetailProgramSerializer
        else:
            return self.serializer_class
    def get_queryset(self):
        if not self.request.query_params.get("sort-by"):
            return Program.objects.order_by("title")
        else:
            if self.request.query_params["sort-by"]=="category":
                qs = Program.objects.order_by("category")
                pk_list = []
                for q in qs:
                    if str(q.uuid) not in pk_list:
                        pk_list.append(str(q.uuid))
                preserved = Case(*[When(uuid=val, then=pos) for pos, val in enumerate(pk_list)], default=len(pk_list))
                qs_out = Program.objects.filter(uuid__in=pk_list).order_by(preserved)
                return qs_out
            elif self.request.query_params["sort-by"]=="-category":
                qs = Program.objects.order_by("-category")
                pk_list = []
                for q in qs:
                    if str(q.uuid) not in pk_list:
                        pk_list.append(str(q.uuid))
                preserved = Case(*[When(uuid=val, then=pos) for pos, val in enumerate(pk_list)], default=len(pk_list))
                qs_out = Program.objects.filter(uuid__in=pk_list).order_by(preserved)
                return qs_out
            else:
                return super().get_queryset()

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
