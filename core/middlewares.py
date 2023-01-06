from typing import Type

from django.conf import settings
from django.http import HttpResponse

from core.utils import get_request_ip, get_ip_info


class RestrictCountryMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):

        print("Request ip:", get_request_ip(request))

        if not self._check_restriction(request):
            return HttpResponse("Forbidden", status=403)

        response = self.get_response(request)  # View call

        return response

    def _check_restriction(self, request):
        client_ip = get_request_ip(request)
        ip_info = get_ip_info(client_ip)  # -> {...,"country":"IR", ...}

        if 'country' in ip_info and ip_info['country'] in self._get_restricted_country_list():
            return False
        else:
            return True

    def _get_restricted_country_list(self):
        return getattr(settings, 'RESTRICTED_COUNTRY_CODES', [])