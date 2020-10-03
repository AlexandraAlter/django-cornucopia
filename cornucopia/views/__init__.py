from django import http


def in_development(request, *args, **kwargs):
    return http.HttpResponse("Not implemented", status=500)
