# coding: utf8
from django.db.models.signals import class_prepared
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MultiDomainConfig(AppConfig):
    name = "multidomain"
    verbose_name = _("MultiDomain")

    def ready(self):
        super(MultiDomainConfig, self).ready()
        class_prepared.send(self.get_model("Domain"))  # send signal, for register actual domain model
