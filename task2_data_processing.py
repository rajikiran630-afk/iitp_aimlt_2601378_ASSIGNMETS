# task2_data_processing.py

# TrendPulse Task 2

# Load JSON data from Task 1, clean it using Pandas,

# and save the cleaned result as CSV.



import pandas as pd

import glob

import os



# Folder where JSON files are stored

DATA_FOLDER = "data"





def find_latest_json_file():

  """

  Find the latest trends_YYYYMMDD.json file inside data folder.

  """

  json_files = glob.glob(os.path.join(DATA_FOLDER, "trends_*.json"))



  if not json_files:

    print("No JSON files found in data folder.")

    return None



  # Sort and return latest file

  json_files.sort()

  return json_files[-1]





def main():

  # Step 1: Find latest JSON file

  json_file = find_latest_json_file()



  if not json_file:

    return



  # Load JSON into DataFrame

  df = pd.read_json(json_file)



  print(f"Loaded {len(df)} stories from {json_file}")



  # -------------------------------

  # Step 2: Clean the Data

  # -------------------------------



  # Remove duplicate post_id rows

  df = df.drop_duplicates(subset="post_id")

  print(f"After removing duplicates: {len(df)}")



  # Remove rows with missing required values

  df = df.dropna(subset=["post_id", "title", "score"])

  print(f"After removing nulls: {len(df)}")



  # Strip extra whitespace from titles

  df["title"] = df["title"].astype(str).str.strip()



  # Convert score and num_comments to integers

  df["score"] = df["score"].astype(int)

  df["num_comments"] = df["num_comments"].fillna(0).astype(int)



  # Remove low-quality stories (score < 5)

  df = df[df["score"] >= 5]

  print(f"After removing low scores: {len(df)}")



  # -------------------------------

  # Step 3: Save cleaned CSV

  # -------------------------------



  output_file = os.path.join(DATA_FOLDER, "trends_clean.csv")

  df.to_csv(output_file, index=False)



  print(f"\nSaved {len(df)} rows to {output_file}")



  # Print category summary

  print("\nStories per category:")

  print(df["category"].value_counts())





# Run script

if __name__ == "__main__":

  main()
