from firebase_config import db

# Register User
def register_user(username, hashed_password):
    users_ref = db.collection("users")
    user_doc = users_ref.document(username).get()

    if user_doc.exists:
        return {"error": "User already exists"}

    users_ref.document(username).set({"username": username, "password": hashed_password})
    return {"message": "User registered successfully!"}

# Get User Data
def get_user(username):
    user_ref = db.collection("users").document(username)
    user_doc = user_ref.get()

    if not user_doc.exists:
        return None

    return user_doc.to_dict()

# Add Step Record for a User
def add_step_record(username, date, steps):
    user_ref = db.collection("users").document(username)
    if not user_ref.get().exists:
        return {"error": "User not found"}

    steps_ref = user_ref.collection("steps").document(date)
    steps_ref.set({"date": date, "steps": steps})

    return {"message": "Step record added!"}

# Get Step Records for a User
def get_step_records(username):
    user_ref = db.collection("users").document(username)
    if not user_ref.get().exists:
        return None

    steps_ref = user_ref.collection("steps").stream()
    return [{"date": doc.id, "steps": doc.to_dict()["steps"]} for doc in steps_ref]
