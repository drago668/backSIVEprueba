from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role.name == 'Admin'

class IsOwnerUser(BasePermission):
    """
    Allows access only to the owner of the object.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role.name == 'Dueno'

class IsRegularUser(BasePermission):
    """
    Allows access only to regular users.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role.name == 'Usuario'
    
class IsActiveUser(BasePermission):
    """
    Allows access only to active users.
    """
    message = 'La cuenta de usuario no está activa.'

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.state.name == 'Activo'