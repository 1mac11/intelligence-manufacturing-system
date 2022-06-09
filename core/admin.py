from django.contrib import admin

from core.models import Territory, Status, FactoryType, Factory

admin.site.register(Territory)
admin.site.register(Status)
admin.site.register(FactoryType)
admin.site.register(Factory)
