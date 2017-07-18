# coding: utf8
import re

from django.utils.deprecation import MiddlewareMixin

from .models import domain_class
from .http import get_domain


class GetDomainMiddleware(MiddlewareMixin):
    """
    Add request.host with subdomain value or None

    """

    def __init__(self, *args, **kwargs):
        """
        Runs one time at the first request

        """
        super(GetDomainMiddleware, self).__init__(*args, **kwargs)
        self.ipv4_re = re.compile(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:?[0-9]{0,5}$")

    def process_request(self, request):
        request.get_domain = get_domain  # Add function, get_domain from request object
        domain, sub_domains = request.META['HTTP_HOST'], request.META['HTTP_HOST'].split('.')
        count = 2

        # TODO: Предусматриваем вариант обращения по IP а не по домену
        if re.match(self.ipv4_re, domain):
            count += 3

        try:
            request.domain = domain_class.objects.filter(
                domain=".".join(sub_domains[:count - 1])
            )
        except domain_class.DoesNotExist:
            request.domain = None
