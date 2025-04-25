from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import uuid
from datetime import date


def get_upload_path(instance, filename):
    """Generate a unique path for uploaded files"""
    # Use instance.id if available, otherwise use a temporary identifier
    if instance.id:
        folder_name = f'project_{instance.id}'
    else:
        # Use a UUID to ensure uniqueness for new projects
        folder_name = f'project_temp_{uuid.uuid4().hex[:10]}'
    return os.path.join('documents', folder_name, filename)


class Project(models.Model):
    """Model for storing project complaint details"""
    project_name = models.CharField(
        max_length=100,
        verbose_name="Project Name",
        help_text="Name of the project"
    )
    short_info = models.CharField(
        max_length=200,
        verbose_name="Short Info",
        help_text="Brief description of the project"
    )
    program = models.TextField(
        max_length=1000,
        verbose_name="Program",
        help_text="Detailed program description"
    )
    started_date = models.DateField(
        verbose_name="Started Date",
        help_text="Date when the project started"
    )
    deadline_date = models.DateField(
        verbose_name="Deadline Date",
        help_text="Expected completion date of the project"
    )
    identification_no = models.CharField(
        max_length=50,
        verbose_name="Identification No",
        help_text="Unique identification number for the project"
    )
    selected_contractor = models.CharField(
        max_length=100,
        verbose_name="Selected Contractor",
        help_text="Name of the contractor working on the project"
    )
    related_document = models.FileField(
        upload_to=get_upload_path,
        blank=True,
        null=True,
        verbose_name="Related Document",
        help_text="Any relevant document for the project"
    )
    remarks = models.TextField(
        max_length=400,
        verbose_name="Remarks",
        blank=True,
        help_text="Additional notes about the project"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects_created',
        verbose_name="Created By",
        help_text="User who created this project"
    )
    
    def __str__(self):
        return f"{self.project_name} (ID: {self.identification_no})"
    
    def clean(self):
        """Validate that deadline_date is after started_date"""
        if self.deadline_date and self.started_date:
            if self.deadline_date < self.started_date:
                raise ValidationError("Deadline date must be after the start date.")
        if self.deadline_date and self.deadline_date < date.today():
            raise ValidationError("Deadline date cannot be in the past.")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        unique_together = ('identification_no',)  # Ensure ID is unique


class Comment(models.Model):
    """Model for storing comments on projects"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_comments',
        verbose_name="Project",
        help_text="Project this comment belongs to"
    )
    text = models.TextField(
        max_length=1000,
        verbose_name="Comment Text",
        help_text="Content of the comment"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_comments',
        verbose_name="Created By",
        help_text="User who created this comment"
    )
    
    def __str__(self):
        return f"Comment by {self.created_by.username} on {self.project.project_name} ({self.created_at.date()})"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"