# Library Management System

A Django-based Library Management System that provides a robust API for managing books, users, and borrowing operations.

## Tech Stack

- **Framework**: Django 5.0.2
- **Database**: MySQL
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (djangorestframework-simplejwt 5.3.1)
- **CORS**: django-cors-headers 4.3.1
- **Environment Variables**: python-dotenv 1.0.1

## Project Structure

```
library_management/
├── books/                  # Main app for book management
├── library_management/     # Project configuration
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── .env                  # Environment variables (not tracked in git)
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd library_management
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate

   # Linux/Mac
   python -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Assumptions

1. The system uses MySQL as the database backend
2. JWT authentication is implemented for secure API access
3. CORS is enabled for cross-origin requests
4. Environment variables are used for sensitive configuration
5. The project follows Django's recommended project structure
