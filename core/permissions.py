from rest_framework.permissions import BasePermission


class SelfPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_anonymous:
            return False
        if request.method == 'GET':
            return user.is_staff or obj.id == user.id
        elif request.method == 'POST':
            return False

