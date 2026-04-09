# Job Board API

A REST API I built using Django and Django REST Framework.

## What it does
- Users can register as Company or Job Seeker
- Companies can post jobs
- Job Seekers can apply to jobs
- JWT authentication
- Search and filter jobs
- Swagger API docs

## Tech Used
- Python, Django 4.2
- Django REST Framework
- SimpleJWT
- SQLite
- Swagger (drf-spectacular)

## How to run it

git clone https://github.com/YOUR_USERNAME/job-board-api
cd job-board-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/users/register/ | POST | Register |
| /api/users/login/ | POST | Login |
| /api/jobs/ | GET | List jobs |
| /api/jobs/ | POST | Create job |
| /api/applications/ | POST | Apply to job |
| /api/docs/ | GET | Swagger docs |

## Admin Panel
http://127.0.0.1:8000/admin/