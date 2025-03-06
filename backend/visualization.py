import matplotlib.pyplot as plt
import seaborn as sns

def plot_step_trend(df):
    plt.figure(figsize=(10,5))
    sns.lineplot(x=df["date"], y=df["steps"], marker="o")
    plt.xlabel("Date")
    plt.ylabel("Step Count")
    plt.title("Daily Step Count Trends")
    plt.xticks(rotation=45)
    plt.show()