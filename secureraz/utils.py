from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthAndOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # Allow safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow authenticated user
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        # Allow safe methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow if user is owner of object
        if not isinstance(obj, User):
            return request.user == obj.user

        # Allow if user is object
        return request.user == obj


class IsAuthAndOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
