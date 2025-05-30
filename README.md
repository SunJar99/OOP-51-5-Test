# Django Blog API

This project is a simple REST API for a blogging platform built using Django and Django Rest Framework (DRF). It allows users to create, read, update, and delete blog posts and comments.

## Features

- User authentication using JWT or token-based authentication.
- CRUD operations for blog posts.
- Ability to add comments to posts.
- Pagination for listing posts.
- Only authorized users can create or modify posts and comments.
- Public access to read published posts.

## Project Structure

```
django-blog-api
├── blog                # Blog application
│   ├── models.py      # Data models for User, Post, and Comment
│   ├── serializers.py  # Serializers for converting models to JSON
│   ├── views.py       # View logic for handling requests
│   ├── urls.py        # URL routing for the blog app
│   ├── permissions.py  # Custom permissions for API access
│   ├── tests.py       # Tests for the application
│   └── migrations      # Database migrations
├── django_blog_api     # Main Django project
│   ├── settings.py    # Project settings and configuration
│   ├── urls.py        # Main URL routing for the project
│   └── wsgi.py        # WSGI configuration
├── manage.py           # Command-line utility for Django
├── Dockerfile          # Dockerfile for building the application image
├── docker-compose.yml  # Docker Compose configuration
└── requirements.txt    # Python dependencies
```

## Installation

### Without Docker

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-blog-api
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

### With Docker

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-blog-api
   ```

2. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

3. Access the application at `http://localhost:8000`.

## API Documentation

API documentation is automatically generated using Swagger/OpenAPI. You can access it at `http://localhost:8000/swagger/` after running the server.

## Testing

To run tests, use the following command:
```
python manage.py test
```

## License

This project is licensed under the MIT License.