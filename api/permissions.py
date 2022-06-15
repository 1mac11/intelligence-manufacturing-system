from rest_framework.permissions import BasePermission

from core.models.user_role import UserRoleChoice


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role.name == UserRoleChoice.OWNER


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role.name == UserRoleChoice.ADMIN


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role.name == UserRoleChoice.STAFF


class IsOutsource(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role.name == UserRoleChoice.OUTSOURCE
