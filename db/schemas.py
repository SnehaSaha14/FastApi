def individual_user(user):
    return {
        "name": str(user.get("name")),
        "email": user.get("email"),
        "password": user.get("password"),
        "status": user.get("is_complete", False) 
    }

def all_users(users):
    return [individual_user(user) for user in users]
