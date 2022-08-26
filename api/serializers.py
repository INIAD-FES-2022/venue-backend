from rest_framework import serializers
from .models import Program, Notice, Group, Category, Image, Link

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url']

class DetailProgramSerializer(serializers.ModelSerializer):
    relatedUrl = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = '__all__'

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

class DetailNoticeSerializer(serializers.ModelSerializer):
    relatedUrl = serializers.SerializerMethodField()
    
    class Meta:
        model = Notice
        fields = '__all__'

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