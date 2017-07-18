# coding: utf8
from django.contrib import admin

from .models import domain_class


@admin.register(domain_class)
class DomainAdmin(admin.ModelAdmin):
    pass
