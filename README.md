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


API ENDPOINTS:

Method |         Endpoint                               | Description

GET    | /api/projects/                         | List all projects
POST   | /api/projects/                         | Create a new project
GET    | /api/projects/<project_id>/            | Retrieve a specific project
PUT    | /api/projects/<project_id>/            | Update a specific project
DELETE | /api/projects/<project_id>/            | Delete a specific project

Method          | Endpoint                                           | Description

GET     | /api/projects/<project_id>/comments/          | List comments under a specific project
POST    | /api/projects/<project_id>/comments/      | Create a comment for a specific project
GET     | /api/projects/<project_id>/comments/<comment_id>/ | Retrieve a specific comment
PUT     | /api/projects/<project_id>/comments/<comment_id>/ | Update a specific comment
DELETE  | /api/projects/<project_id>/comments/<comment_id>/ | Delete a specific comment