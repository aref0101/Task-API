# Taskmaster API

A Django REST Framework–based web API for creating, viewing, editing, and deleting to-do tasks. Only the authenticated owner of a task is authorized to modify or delete it. The system includes user login and registration, JWT-based authentication, and a full suite of features such as pagination, filtering, search, ordering, request throttling, and API versioning.

---

## Features

- **User Auth**  
User registration and login are implemented using JSON Web Tokens (JWT) via Simple JWT, with full support for token refresh and rotation to ensure secure and seamless authentication.

- **Tasks CRUD**  
  - **Create** a new task  
  - **Read** (list/detail) your tasks  
  - **Update** or **Partial Update** only if you’re the owner  
  - **Delete** only your own tasks

- **API Niceties**  
  - **Pagination**: Flexible and configurable page sizes to suit varying client needs.  
  - **Filter** & **Search**: Query your tasks by title, description, or any other field you’ve got.  
  - **Ordering**: Ordering: Allows clients to sort task results by specified fields, such as creation date, to display tasks in a desired order (e.g., oldest first). 
  - **Throttling**: Prevents from hammering the API.  
  - **Versioning**: backward-incompatible changes require clear and structured communication.

---

## Tech Stack

- **Python 3.x**  
- **Django 4.x**  
- **Django REST Framework**  
- **djangorestframework-simplejwt**  
- **SQLite** 
- **django-filter**  

---

## 📥 Installation

1. **Clone it**  
   ```bash
   git clone https://github.com/aref0101/Django-rest-framework-project.git
   cd Django-rest-framework-project

# 2. Create & activate a virtualenv
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
SECRET_KEY=your-django-secret-key-avoid-using-‘django-insecure’
DEBUG=True   # switch to False in prod
ALLOWED_HOSTS=127.0.0.1,localhost

# 5. python manage.py migrate
python manage.py migrate

# 6. Create a superuser
python manage.py createsuperuser

# 7. start the project
python manage.py runserver