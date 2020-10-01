from django import http

from . import boards
from . import posts


def in_development(request, *args, **kwargs):
    return http.HttpResponse("Not implemented", status=500)
