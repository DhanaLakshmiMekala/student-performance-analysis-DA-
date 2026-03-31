import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("students_scores.csv")

# Drop unwanted column
df = df.drop("Unnamed: 0", axis=1)

# Fix data issue
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "5-10")

# -------------------------------
# Basic Info
# -------------------------------
print(df.head())
print(df.describe())
print(df.isnull().sum())

# -------------------------------
# Gender Distribution
# -------------------------------
plt.figure(figsize=(4,5))
ax = sns.countplot(data=df, x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()

# -------------------------------
# Parent Education vs Scores
# -------------------------------
gb = df.groupby("ParentEduc").agg({
    "MathScore": "mean",
    "ReadingScore": "mean",
    "WritingScore": "mean"
})

plt.figure(figsize=(6,4))
sns.heatmap(gb, annot=True)
plt.title("Parent Education vs Student Scores")
plt.show()

# -------------------------------
# Parent Marital Status vs Scores
# -------------------------------
gb1 = df.groupby("ParentMaritalStatus").agg({
    "MathScore": "mean",
    "ReadingScore": "mean",
    "WritingScore": "mean"
})

plt.figure(figsize=(6,4))
sns.heatmap(gb1, annot=True)
plt.title("Parent Marital Status vs Scores")
plt.show()

# -------------------------------
# Score Distribution
# -------------------------------
sns.boxplot(data=df, x="MathScore")
plt.title("Math Score Distribution")
plt.show()

sns.boxplot(data=df, x="ReadingScore")
plt.title("Reading Score Distribution")
plt.show()

# -------------------------------
# Ethnic Group Distribution (Pie)
# -------------------------------
group_counts = df["EthnicGroup"].value_counts()

plt.pie(group_counts, labels=group_counts.index, autopct="%1.1f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()

# -------------------------------
# Ethnic Group Count Plot
# -------------------------------
ax = sns.countplot(data=df, x="EthnicGroup")
ax.bar_label(ax.containers[0])
plt.title("Ethnic Group Count")
plt.show()