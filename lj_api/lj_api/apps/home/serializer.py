from rest_framework.serializers import ModelSerializer

from .models import Banner, Nav


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ("img", "link")


class HeaderFooterSerializer(ModelSerializer):
    class Meta:
        model=Nav
        fields=('title','link','position','is_site')
