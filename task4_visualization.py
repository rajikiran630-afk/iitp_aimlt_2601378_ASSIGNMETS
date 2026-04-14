# task4_visualization.py

# TrendPulse Task 4

# Load analysed CSV data and create visualizations using Matplotlib



import pandas as pd

import matplotlib.pyplot as plt

import os



# File paths

INPUT_FILE = "data/trends_analysed.csv"

OUTPUT_FOLDER = "outputs"



# Create outputs folder if it does not exist

os.makedirs(OUTPUT_FOLDER, exist_ok=True)





def shorten_title(title, max_length=50):

  """

  Shorten long story titles so they fit neatly in charts.

  """

  return title if len(title) <= max_length else title[:47] + "..."





def main():

  # -------------------------------

  # Step 1: Load Data

  # -------------------------------

  df = pd.read_csv(INPUT_FILE)



  # -------------------------------

  # Chart 1: Top 10 Stories by Score

  # -------------------------------

  top_stories = df.nlargest(10, "score").copy()

  top_stories["short_title"] = top_stories["title"].apply(shorten_title)



  plt.figure(figsize=(10, 6))

  plt.barh(top_stories["short_title"], top_stories["score"])

  plt.xlabel("Score")

  plt.ylabel("Story Title")

  plt.title("Top 10 Stories by Score")

  plt.gca().invert_yaxis()

  plt.tight_layout()

  plt.savefig(f"{OUTPUT_FOLDER}/chart1_top_stories.png")

  plt.close()



  # -------------------------------

  # Chart 2: Stories per Category

  # -------------------------------

  category_counts = df["category"].value_counts()



  plt.figure(figsize=(8, 5))

  plt.bar(category_counts.index, category_counts.values,

      color=["blue", "green", "red", "orange", "purple"])

  plt.xlabel("Category")

  plt.ylabel("Number of Stories")

  plt.title("Stories per Category")

  plt.tight_layout()

  plt.savefig(f"{OUTPUT_FOLDER}/chart2_categories.png")

  plt.close()



  # -------------------------------

  # Chart 3: Score vs Comments Scatter

  # -------------------------------

  popular = df[df["is_popular"] == True]

  non_popular = df[df["is_popular"] == False]



  plt.figure(figsize=(8, 6))

  plt.scatter(non_popular["score"], non_popular["num_comments"],

        color="gray", label="Not Popular")

  plt.scatter(popular["score"], popular["num_comments"],

        color="red", label="Popular")



  plt.xlabel("Score")

  plt.ylabel("Number of Comments")

  plt.title("Score vs Comments")

  plt.legend()

  plt.tight_layout()

  plt.savefig(f"{OUTPUT_FOLDER}/chart3_scatter.png")

  plt.close()



  # -------------------------------

  # Bonus: Combined Dashboard

  # -------------------------------

  fig, axes = plt.subplots(1, 3, figsize=(18, 6))

  fig.suptitle("TrendPulse Dashboard", fontsize=16)



  # Dashboard Chart 1

  axes[0].barh(top_stories["short_title"], top_stories["score"])

  axes[0].set_title("Top 10 Stories")

  axes[0].set_xlabel("Score")

  axes[0].set_ylabel("Title")

  axes[0].invert_yaxis()



  # Dashboard Chart 2

  axes[1].bar(category_counts.index, category_counts.values,

        color=["blue", "green", "red", "orange", "purple"])

  axes[1].set_title("Stories per Category")

  axes[1].set_xlabel("Category")

  axes[1].set_ylabel("Count")

  axes[1].tick_params(axis='x', rotation=45)



  # Dashboard Chart 3

  axes[2].scatter(non_popular["score"], non_popular["num_comments"],

          color="gray", label="Not Popular")

  axes[2].scatter(popular["score"], popular["num_comments"],

          color="red", label="Popular")

  axes[2].set_title("Score vs Comments")S

  axes[2].set_xlabel("Score")

  axes[2].set_ylabel("Comments")

  axes[2].legend()



  plt.tight_layout(rect=[0, 0, 1, 0.95])

  plt.savefig(f"{OUTPUT_FOLDER}/dashboard.png")

  plt.close()



  print("All charts created successfully in outputs/ folder")





# Run script

if __name__ == "__main__":

  main()
