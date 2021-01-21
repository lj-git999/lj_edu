from rest_framework.generics import ListAPIView

from .models import Banner, Nav
from .serializer import BannerSerializer, HeaderFooterSerializer


class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerSerializer


class HeaderAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, position=1).order_by("-orders")
    serializer_class = HeaderFooterSerializer


class FooterAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, position=2).order_by("-orders")
    serializer_class = HeaderFooterSerializer
