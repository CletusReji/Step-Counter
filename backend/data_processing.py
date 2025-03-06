import pandas as pd
from database import add_step_record

def preprocess_and_upload_csv(filepath, username):
    try:
        # Load CSV file
        df = pd.read_csv(filepath)

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower()

        # Ensure required columns exist
        required_columns = {"date", "steps"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns: {required_columns - set(df.columns)}")

        # Convert date column to proper format
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")

        # Remove invalid dates
        df = df.dropna(subset=["date"])

        # Convert steps to integer, replacing non-numeric values with NaN, then dropping NaNs
        df["steps"] = pd.to_numeric(df["steps"], errors="coerce").fillna(0).astype(int)

        # Remove negative or unrealistic step values
        df = df[df["steps"] >= 0]

        # Upload each step record to Firebase under the user's collection
        for _, row in df.iterrows():
            add_step_record(username, row["date"], row["steps"])

        return {"message": "CSV data uploaded successfully!"}

    except Exception as e:
        return {"error": f"Error processing CSV: {e}"}

# Example Usage:
# preprocess_and_upload_csv("data/step_data.csv", "test_user")
