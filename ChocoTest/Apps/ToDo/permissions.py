from rest_framework import permissions


class IsEmployeeUser(permissions.BasePermission):
    """
    Allows access only to employee users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_employee)


class IsAdministratorUser(permissions.BasePermission):
    """
    Allows access only to employee users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_administrator)

