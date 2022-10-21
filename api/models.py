import uuid
from django.db import models

class Group(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    homepage = models.URLField(blank=True)
    logo = models.ImageField(upload_to="")

    def __str__(self):
        return self.name


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    is_for_notice = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    content = models.TextField(max_length = 1000)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Program(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    streaming_url = models.URLField(blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    thumbnail = models.ImageField(upload_to="", null=True, blank=True)
    is_online = models.BooleanField(default=True)
    is_face2face = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    url = models.URLField()
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    program = models.ForeignKey(Program, blank=True, null=True, on_delete=models.SET_NULL)
    notice = models.ForeignKey(Notice, blank=True, null=True, on_delete=models.SET_NULL)


class Image(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")
