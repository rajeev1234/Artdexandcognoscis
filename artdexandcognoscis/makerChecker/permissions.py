
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS or request.method == 'PUT'):
            return True

        # Write permissions are only allowed to the owner of the snippet.
        if request.method == "PUT" and request.user.is_checker:
            return obj.user == request.user
        if request.method == "POST" and request.user.is_maker:
            return obj.user == request.user
        if request.method == "GET" and request.user.is_maker:
            return obj.user == request.user
        return False

class IsChecker(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is checker
        return view.action == 'retrieve' or request.user.is_checker

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_checker


class IsMaker(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is maker
        return view.action == 'retrieve' or request.user.is_maker

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_maker