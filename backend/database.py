from firebase_config import db

def add_step_record(date, steps):
    """Add a step count record to Firebase Firestore."""
    doc_ref = db.collection("step_records").document(date)
    doc_ref.set({"date": date, "steps": steps})

def get_step_records():
    """Retrieve all step records from Firebase."""
    docs = db.collection("step_records").stream()
    step_data = [{"date": doc.id, "steps": doc.to_dict()["steps"]} for doc in docs]
    return step_data