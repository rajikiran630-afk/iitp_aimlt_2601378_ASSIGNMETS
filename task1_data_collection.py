# task1_data_collection.py

# TrendPulse Task 1

# Fetch trending HackerNews stories, classify them into categories,

# and save the collected data into a JSON file.



import requests

import json

import os

import time

from datetime import datetime



# Base HackerNews API URLs

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"

ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"



# Request header required in assignment

headers = {

  "User-Agent": "TrendPulse/1.0"

}



# Category keywords (case-insensitive match)

CATEGORIES = {

  "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],

  "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],

  "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],

  "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],

  "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]

}



MAX_PER_CATEGORY = 25





def get_top_story_ids():

  """Fetch first 500 top story IDs from HackerNews."""

  try:

    response = requests.get(TOP_STORIES_URL, headers=headers)

    response.raise_for_status()

    return response.json()[:500]

  except requests.RequestException as e:

    print(f"Failed to fetch top stories: {e}")

    return []





def get_story_details(story_id):

  """Fetch details for a single story by ID."""

  try:

    response = requests.get(ITEM_URL.format(story_id), headers=headers)

    response.raise_for_status()

    return response.json()

  except requests.RequestException as e:

    print(f"Failed to fetch story {story_id}: {e}")

    return None





def assign_category(title):

  """Assign category based on keyword match in title."""

  if not title:

    return None



  title_lower = title.lower()



  for category, keywords in CATEGORIES.items():

    for keyword in keywords:

      if keyword.lower() in title_lower:

        return category



  return None





def main():

  # Fetch top story IDs

  story_ids = get_top_story_ids()



  if not story_ids:

    print("No story IDs fetched. Exiting.")

    return



  collected_stories = []

  category_counts = {category: 0 for category in CATEGORIES}



  # Loop category by category

  for category in CATEGORIES:

    print(f"Collecting category: {category}")



    for story_id in story_ids:

      # Stop if category already has enough stories

      if category_counts[category] >= MAX_PER_CATEGORY:

        break



      story = get_story_details(story_id)



      if not story:

        continue



      title = story.get("title", "")

      matched_category = assign_category(title)



      # Only collect if story belongs to current category

      if matched_category == category:

        collected_stories.append({

          "post_id": story.get("id"),

          "title": title,

          "category": matched_category,

          "score": story.get("score", 0),

          "num_comments": story.get("descendants", 0),

          "author": story.get("by", "unknown"),

          "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        })



        category_counts[category] += 1



    # Sleep once after each category loop

    time.sleep(2)



  # Create data folder if not exists

  os.makedirs("data", exist_ok=True)



  # Generate filename with today's date

  filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"



  # Save data to JSON file

  with open(filename, "w", encoding="utf-8") as file:

    json.dump(collected_stories, file, indent=4)



  # Print final result

  print(f"Collected {len(collected_stories)} stories. Saved to {filename}")





# Run script

if __name__ == "__main__":

  main()
