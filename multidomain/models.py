from distutils.version import LooseVersion

from django import get_version
from django.core.exceptions import AppRegistryNotReady
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class AbstractBaseDomain(models.Model):
    """
    Base Domain class

    """
    domain = models.CharField("Домен сайта", max_length=255)

    class Meta:
        verbose_name = "Домен"
        verbose_name_plural = "Домены"
        abstract = True

    def __str__(self):
        return self.domain

    def __unicode__(self):
        return self.__str__()


class Domain(AbstractBaseDomain):
    """
    Domain model.

    """
    pass


# Get Actual Domain model
domain_class = Domain

if LooseVersion(get_version()) > LooseVersion("1.7"):
    from django.apps import apps
    get_model = getattr(apps, "get_model")
else:
    from django.db.models.loading import get_model


_domain_class_path = getattr(settings, "MULTIDOMAIN_MODEL", None)
if _domain_class_path:
    if len(_domain_class_path.split(".")) != 2:
        raise ValueError(
            "MULTIDOMAIN_MODEL takes two arguments `app_label.model_name`. "
            "%d transferred" % len(_domain_class_path.split("."))
        )

    try:
        new_class = get_model(*_domain_class_path.split("."))
    except AppRegistryNotReady:
        raise ValueError(
            "MULTIDOMAIN_MODEL `%s` not found. Please check your settings." % str(_domain_class_path)
        )
