import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\George Samvel\\Desktop\\cleaned_netflix_data.csv")

# Step 1: Remove duplicate rows
df = df.drop_duplicates()

# Step 2: Drop rows with critical nulls
df = df.dropna(subset=['country', 'rating', 'date_added'])

# Step 3: Standardize text formatting
df['type'] = df['type'].str.strip().str.lower()
df['country'] = df['country'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()

# Step 4: Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Step 5: Rename columns to snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 6: Fix data types
df['release_year'] = df['release_year'].astype(int)

# Step 7: Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

# Print summary
print("✅ Dataset cleaned successfully.")
print("🔢 Final row count:", df.shape[0])
print("🧾 Remaining nulls per column:\n", df.isnull().sum())
print("📁 Cleaned file saved as 'cleaned_netflix_data.csv'")
