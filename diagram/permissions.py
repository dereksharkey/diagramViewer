from rest_framework import permissions

class TempPermission(permissions.BasePermission):
    """
    Custom permissions - testing
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
