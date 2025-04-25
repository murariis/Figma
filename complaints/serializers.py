from rest_framework import serializers
from .models import Project, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model"""
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['created_at', 'updated_at']


class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating comments"""
    class Meta:
        model = Comment
        fields = ['text']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model"""
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source='project_comments')
    
    class Meta:
        model = Project
        fields = [
            'id', 'project_name', 'short_info', 'program', 'started_date', 
            'deadline_date', 'identification_no', 'selected_contractor', 
            'related_document', 'remarks', 'created_at', 'updated_at', 
            'created_by', 'comments'
        ]
        read_only_fields = ['created_at', 'updated_at']


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating projects"""
    class Meta:
        model = Project
        fields = [
            'project_name', 'short_info', 'program', 'started_date', 
            'deadline_date', 'identification_no', 'selected_contractor', 
            'related_document', 'remarks'
        ]