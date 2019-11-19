from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Base owner permission"""
    message = "Not an owner."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user
