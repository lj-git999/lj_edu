import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

logger = logging.getLogger("django")


def exception_handler(exc, context):
    error = "%s %s %s" % (context['view'], context["request"].method, exc)
    response = drf_exception_handler(exc, context)
    if response is None:
        logger.error(error)
        return Response({
            "error_msg": "程序内部错误，请稍等一会"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=None)
    return response
