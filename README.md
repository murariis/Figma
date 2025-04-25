# Complaint Management System

A Django REST API based system for managing complaints. This system allows administrators to enter complaints received through letters into the system, and users can login and add comments on the complaint descriptions.

## Features

- Admin can enter complaint details
- User authentication and authorization
- Users can add comments on complaints
- File upload for related documents
- RESTful API for accessing and managing complaints and comments

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`

## API Endpoints

- `/api/projects/` - List and create projects
- `/api/projects/<id>/` - Retrieve, update, and delete a project
- `/api/comments/` - List and create comments
- `/api/comments/<id>/` - Retrieve, update, and delete a comment