import pandas as pd
from database import add_step_record

def upload_csv_to_firebase(filepath="data/step_data.csv"):
    df = pd.read_csv(filepath)
    for _, row in df.iterrows():
        add_step_record(row["date"], int(row["steps"]))

# Run this function once to upload CSV data
upload_csv_to_firebase()