from rest_framework.permissions import BasePermission

class AllowTokenFreeAccess(BasePermission):
    token_free_paths = [
        '/api/usuario-create',
        '/api/usuario-validar-contra',
        '/api/adopcion-list'
    ]

    def has_permission(self, request, view):
        # Allow access without token to the specified paths
        if request.path in self.token_free_paths:
            return True
        # Otherwise, enforce authentication
        return request.user and request.user.is_authenticated