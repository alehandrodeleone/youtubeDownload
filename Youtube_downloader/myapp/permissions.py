from rest_framework.permissions import BasePermission

class Permissions_link(BasePermission):
   def has_object_permission(self, request, view, obj):
       return request(request.user==obj.user)