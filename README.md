
```markdown
# FastAPI + MongoDB Atlas Project
# FastAPI + MongoDB Atlas Project

![Python](https://img.shields.io/badge/Python-3.14.5-blue?logo=python&logoColor=white)  
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)  
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen?logo=mongodb)  




## 🚀 Overview
This project is a FastAPI application connected to MongoDB Atlas.  
It demonstrates CRUD operations (Create, Read, Update, Delete) with user data.

## ⚙️ Tech Stack
- **FastAPI**  
- **PyMongo**  
- **MongoDB Atlas**  
- **Python 3.14.5**  

```
## 📂 Project Structure
```
📂 FastApi/
├── 📄 main.py            - Entry point of FastAPI app
├── 📄 config.py          - MongoDB Atlas connection setup
├── 📄 models.py          - Database models / logic
├── 📄 schemas.py         - Pydantic schemas (request/response validation)
├── 📄 requirements.txt   - Python dependencies
├── 📄 README.md          - Project documentation
├── 📂 venv/              - Virtual environment
└── 📂 __pycache__/       - Compiled Python files
```

---

## ▶️ Running the Project

### 🔽 Clone the repo
```bash
git clone https://github.com/SnehaSaha14/FastApi.git
cd FastApi
```

### 🛠️ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 📦 Install dependencies
```bash
pip install -r requirements.txt
```

### 🚀 Run the server
```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation
Once the server is running, open your browser and visit:  
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  

This will show the **interactive Swagger UI** where you can test all endpoints.

---

## 📌 Features
- **User creation** with unique email  
- **Update user** by email or name  
- Auto‑update **`updated_at` timestamp**  
- Secure **MongoDB Atlas connection**  

---

## 📝 Git Commands
Stage and commit:
```bash
git add .
git commit -m "Initial commit: FastAPI project"
git push -u origin main
```
