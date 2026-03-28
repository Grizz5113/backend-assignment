# 🚀 Backend Assignment – Django REST API

## 📌 Features

* JWT Authentication (Login/Register)
* Role-Based Access (Admin/User)
* Task CRUD APIs
* Protected Endpoints

## 🛠 Tech Stack

* Python, Django, DRF
* SimpleJWT
* SQLite

## ⚙️ Setup

```bash
git clone <repo-link>
cd backend-assignment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔐 Auth APIs

* POST `/api/v1/auth/register/`
* POST `/api/v1/auth/login/`

## 📦 Task APIs

* GET `/api/v1/tasks/`
* POST `/api/v1/tasks/`

## 🔑 Authorization

```
Authorization: Bearer <token>
```

## 👨‍💻 Author

Harsh
