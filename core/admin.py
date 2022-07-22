from django.contrib import admin

from core.models import (
    Territory,
    Status,
    FactoryType,
    Factory,
    Building,
    BuildingType,
    MachineToolType,
    MachineTool,
    Team,
    User,
    UserDetail,
    UserType,
    UserRole
)

admin.site.register(Territory)
admin.site.register(Status)
admin.site.register(FactoryType)
admin.site.register(Factory)
admin.site.register(Building)
admin.site.register(BuildingType)
admin.site.register(MachineToolType)
admin.site.register(MachineTool)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(UserDetail)
admin.site.register(UserType)
admin.site.register(UserRole)
