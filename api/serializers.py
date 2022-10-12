from rest_framework import serializers
from .models import Program, Notice, Group, Image, Category, Link

class ProgramSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = ["uuid", "title", "start_at", "end_at", "place", "group", "category", "thumbnail"]
    
    def get_group(self, obj):
        try:
            group = Group.objects.get(uuid=obj.group.uuid)
            serializer = SimpleGroupSerializer(group)
            return serializer.data
        except:
            return ""

    def get_category(self, obj):
        try:
            cats = obj.category.all()
            serializer = SimpleCategorySerializer(cats, many=True)
            return serializer.data
        except:
            return ""
    

class NoticeSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Notice

        fields = ["uuid", "title", "date", "category"]
 
    def get_category(self, obj):
        try:
            cats = obj.category.all()
            serializer = SimpleCategorySerializer(cats, many=True)
            return serializer.data
        except:
            return ""

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["uuid", "name", "logo"]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']

class SimpleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name", "uuid"]

class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "uuid"]

class DetailProgramSerializer(serializers.ModelSerializer):
    relatedUrl = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = ["group", "title", "description", "start_at", "end_at", "streaming_url", "relatedUrl", "logo", "category", "place", "images", "thumbnail"]

    def get_relatedUrl(self, obj):
        try:
            links = Link.objects.filter(program=obj.pk)
            serializer = LinkSerializer(links, many=True)
            output=[]
            for link_obj in serializer.data:
                output.append(link_obj["url"])
            return output
        except:
            return ""

    def get_images(self, obj):
        try:
            imgs = Image.objects.filter(program=obj.pk)
            serializer = ImageSerializer(imgs, many=True)
            output=[]
            for img_obj in (serializer.data):
                adj_img_obj = self.context['request']._current_scheme_host + img_obj["image"]
                # もしくはadj_img_obj = "https://api.iniadfes.com" + img_obj["image"]
                output.append(adj_img_obj)
            return output
        except:
            return ""

    def get_group(self, obj):
        try:
            group = Group.objects.get(uuid=obj.group.uuid)
            serializer = SimpleGroupSerializer(group)
            return serializer.data
        except:
            return ""
            
    def get_category(self, obj):
        try:
            cats = obj.category.all()
            serializer = SimpleCategorySerializer(cats, many=True)
            return serializer.data
        except:
            return ""

    def get_logo(self, obj):
        try:
            img = Group.objects.get(uuid=obj.group.uuid)
            serializer = GroupSerializer(img)
            return self.context['request']._current_scheme_host + serializer.data["logo"]
        except:
            return ""


class DetailNoticeSerializer(serializers.ModelSerializer):
    relatedUrl = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Notice
        fields = ["uuid", "title", "date", "category", "content", "relatedUrl"]

    def get_relatedUrl(self, obj):
        try:
            links = Link.objects.filter(notice=obj.pk)
            serializer = LinkSerializer(links, many=True)
            output=[]
            for link_obj in (serializer.data):
                output.append(link_obj["url"])
            return output
        except:
            return ""

    def get_category(self, obj):
        try:
            cats = obj.category.all()
            serializer = SimpleCategorySerializer(cats, many=True)
            return serializer.data
        except:
            return ""

class DetailGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name", "description", "homepage", "logo"]
