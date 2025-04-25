from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

# Create a router for the Project viewset
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

# Create a nested router for comments within projects
project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'comments', views.CommentViewSet, basename='project-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
]