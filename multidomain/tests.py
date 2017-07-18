# coding: utf8
from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

from .models import domain_class
from .http import get_domain


class TestApp(TestCase):
    def test_models(self):
        self.assertTrue(domain_class.objects.create(domain="localhost"))
        self.assertEqual(domain_class._meta.verbose_name, _("Domain"))

    def test_middleware(self):
        pass

    def test_get_domain(self):
        pass
