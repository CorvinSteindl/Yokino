from .exceptions import Unauthorized
from django.http import HttpResponseForbidden


class UnauthorizedMiddleware:
    def process_exception(self, request, exception):
        if isinstance(exception, Unauthorized):
            return HttpResponseForbidden()
