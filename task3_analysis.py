# task3_analysis.py

# TrendPulse Task 3

# Load cleaned CSV data, analyze using Pandas + NumPy,

# create new columns, and save analysed data.



import pandas as pd

import numpy as np

import os



# File paths

INPUT_FILE = "data/trends_clean.csv"

OUTPUT_FILE = "data/trends_analysed.csv"





def main():

  # -------------------------------

  # Step 1: Load and Explore Data

  # -------------------------------

  df = pd.read_csv(INPUT_FILE)



  print(f"Loaded data: {df.shape}")



  print("\nFirst 5 rows:")

  print(df.head())



  avg_score = df["score"].mean()

  avg_comments = df["num_comments"].mean()



  print(f"\nAverage score  : {avg_score:.2f}")

  print(f"Average comments: {avg_comments:.2f}")



  # -------------------------------

  # Step 2: NumPy Analysis

  # -------------------------------

  scores = df["score"].to_numpy()

  comments = df["num_comments"].to_numpy()



  mean_score = np.mean(scores)

  median_score = np.median(scores)

  std_score = np.std(scores)



  max_score = np.max(scores)

  min_score = np.min(scores)



  # Category with most stories

  top_category = df["category"].value_counts().idxmax()

  top_category_count = df["category"].value_counts().max()



  # Story with most comments

  max_comments_index = np.argmax(comments)

  most_commented_title = df.iloc[max_comments_index]["title"]

  most_comments = df.iloc[max_comments_index]["num_comments"]



  print("\n--- NumPy Stats ---")

  print(f"Mean score  : {mean_score:.2f}")

  print(f"Median score : {median_score:.2f}")

  print(f"Std deviation: {std_score:.2f}")

  print(f"Max score  : {max_score}")

  print(f"Min score  : {min_score}")



  print(f"\nMost stories in: {top_category} ({top_category_count} stories)")



  print(

    f'\nMost commented story: "{most_commented_title}" '

    f'— {most_comments} comments'

  )



  # -------------------------------

  # Step 3: Add New Columns

  # -------------------------------



  # Engagement = num_comments / (score + 1)

  df["engagement"] = df["num_comments"] / (df["score"] + 1)



  # Popular if score > average score

  df["is_popular"] = df["score"] > avg_score



  # -------------------------------

  # Step 4: Save Analysed Data

  # -------------------------------

  os.makedirs("data", exist_ok=True)

  df.to_csv(OUTPUT_FILE, index=False)



  print(f"\nSaved to {OUTPUT_FILE}")





# Run script

if __name__ == "__main__":

  main()
