
# FastAPI + MongoDB Atlas Project

# 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3.14.5-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

---

## 🚀 Overview

This project is a FastAPI application connected to MongoDB Atlas.  
It demonstrates CRUD operations (Create, Read, Update, Delete) with user data.

---

## ⚙️ Tech Stack

- **FastAPI**
- **PyMongo**
- **MongoDB Atlas**
- **Python 3.14.5**

---

## 📂 Project Structure

```bash
📂 FastApi/
├── 📄 main.py            - Entry point of FastAPI app
├── 📄 config.py          - MongoDB Atlas connection setup
├── 📄 models.py          - Database models / logic
├── 📄 schemas.py         - Pydantic schemas
├── 📄 requirements.txt   - Python dependencies
├── 📄 README.md          - Project documentation
├── 📂 venv/              - Virtual environment
└── 📂 __pycache__/       - Compiled Python files
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=your_mongodb_connection_string
DATABASE_NAME=fastapi_db
```

---

## ▶️ Running the Project

### 🔽 Clone the Repository

```bash
git clone https://github.com/SnehaSaha14/FastApi.git
cd FastApi
```

### 🛠️ Create Virtual Environment

```bash
python -m venv venv
```

### ▶️ Activate Virtual Environment

#### Linux / Mac

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🚀 Run the Server

```bash
uvicorn main:app --reload
```

Server will start at:

```bash
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Once the server is running, open:

```bash
http://127.0.0.1:8000/docs
```

Swagger UI will appear where you can test all APIs interactively.

---
## 📌 API Endpoints
| Method | Endpoint      | Description
|--------|---------------|-------------
| GET    | `/users`      | Get all users
| POST   | `/users`      | Create a new user
| PUT    | `/users/{id}` | Update user
| DELETE | `/users/{id}` | Delete user

---

## ✨ Features

- ✅ User CRUD operations
- ✅ MongoDB Atlas integration
- ✅ FastAPI Swagger documentation
- ✅ Pydantic request validation
- ✅ Automatic timestamp updates
- ✅ Clean project structure

---

## 📚 What I Learned

- FastAPI basics
- REST API development
- MongoDB Atlas connection
- CRUD operations
- API testing using Swagger UI
- Pydantic schema validation

---

## 🔮 Future Improvements

- 🔐 JWT Authentication
- 👥 Role-based authorization
- 🐳 Docker deployment
- ✅ Unit testing
- ⚡ CI/CD pipeline
- ☁️ Cloud deployment

---

## 📝 Git Commands

```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 👩‍💻 Author

Made with ❤️ by **Sneha Saha**

🔗 GitHub:  
https://github.com/SnehaSaha14

---

## 📄 License

This project is licensed under the MIT License.
````
