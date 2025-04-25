from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .models import Project, Comment
from .serializers import (
    ProjectSerializer, ProjectCreateUpdateSerializer,
    CommentSerializer, CommentCreateSerializer
)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Project instances."""
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectCreateUpdateSerializer
        return ProjectSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Comment instances."""
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
    
    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk')
        queryset = Comment.objects.all()
        
        if project_pk is not None:
            try:
                project_pk = int(project_pk)
                queryset = queryset.filter(project_id=project_pk)
            except (ValueError, TypeError):
                raise ValidationError("Invalid project ID")
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        try:
            project = get_object_or_404(Project, pk=int(project_id))
            serializer.save(created_by=self.request.user, project=project)
        except (ValueError, TypeError):
            return Response(
                {"error": "Invalid project ID"},
                status=status.HTTP_400_BAD_REQUEST
            )