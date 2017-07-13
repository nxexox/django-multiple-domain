from django.db.models.signals import class_prepared

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MultiDomainConfig(AppConfig):
    name = "multidomain"
    verbose_name = _("MultiDomain")

    def ready(self):
        pass
