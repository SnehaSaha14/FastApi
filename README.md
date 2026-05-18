# FastAPI + MongoDB Atlas Project

![Python](https://img.shields.io/badge/Python-3.14.5-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-brightgreen?logo=mongodb)


## 🚀 Overview
This project is a FastAPI application connected to MongoDB Atlas.  
It demonstrates CRUD operations (Create, Read, Update, Delete) with user data.

---

## ⚙️ Tech Stack
- **[FastAPI](ca://s?q=FastAPI_framework_overview)**  
- **[PyMongo](ca://s?q=PyMongo_library_for_MongoDB)**  
- **[MongoDB Atlas](ca://s?q=MongoDB_Atlas_cloud_database)**  
- **[Python 3.14.5](ca://s?q=Python_3.14.5_features)**  

```
## 📂 Project Structure
FastApi/
├── 📄 main.py            - Entry point of FastAPI app
├── 📄 config.py          - MongoDB Atlas connection setup
├── 📄 models.py          - Database models/logic
├── 📄 schemas.py         - Pydantic schemas (request/response validation)
├── 📄 requirements.txt   - Python dependencies
├── 📄 README.md          - Project documentation
├── 📂 venv/              - Virtual environment
└── 📂 pycache/           - Compiled Python files 

### 🔽 Clone the repo
```bash
git clone https://github.com/SnehaSaha14/FastApi.git

cd FastApi
🛠️ Create a virtual environment

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

🚀Run the server
bash
uvicorn main:app --reload

📌 Features
User creation with unique email
Update user by email or name
Auto‑update updated_at timestamp
Secure MongoDB Atlas connection

📝 Git Commands
Stage and commit:

bash
git add README.md
git commit -m "Add README.md"
git push