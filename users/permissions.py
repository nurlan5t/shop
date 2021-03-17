from rest_framework.permissions import BasePermission

from users.models import CLIENT


class IsClient(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if not request.user.is_anonymous and request.user.role == CLIENT:
            return True
        else:
            return False
