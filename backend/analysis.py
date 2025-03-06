def categorize_activity(df, threshold=7500):
    df["activity_level"] = df["steps"].apply(lambda x: "Active" if x >= threshold else "Inactive")
    return df