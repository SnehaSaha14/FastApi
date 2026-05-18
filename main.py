from fastapi import FastAPI, APIRouter, HTTPException
from config import collection
from db.schemas import all_users
from db.models import User

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_users():
    data = collection.find()
    return all_users(data)

@router.post("/")
async def create_user(user: User):
    try:
        existing_user = list(collection.find({"email": user.email}))
        if existing_user:
            return {"message": "User already exists!"}

        result = collection.insert_one(user.dict())
        return {
            "message": "User created successfully!",
            "id": str(result.inserted_id)  # return unique MongoDB ObjectId
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.put("/")
async def update_user(user: User):
    try:
        result = collection.update_one(
            {"email": user.email}, 
            {"$set": user.dict()}
        )
        if result.matched_count == 0:
            return {"message": "User not found!"}
        return {"message": "User updated successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
@router.delete("/")
async def delete_user(email: str):
    try:
        result = collection.delete_one({"email": email})
        if result.deleted_count == 0:
            return {"message": "User not found!"}
        return {"message": "User deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

app.include_router(router)
