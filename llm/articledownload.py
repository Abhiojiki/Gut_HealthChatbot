import csv
from langchain.document_loaders import UnstructuredURLLoader
import json
import pandas as pd

# Step 1: Read URLs from the combined sitemap CSV
urls = pd.read_csv("./combinedsitemap.csv")["url"].tolist()

# Step 2: Extract content using UnstructuredURLLoader
docs = []
for url in urls:
    try:
        loader = UnstructuredURLLoader(urls=[url])
        docs.extend(loader.load())  # Each document contains .page_content and metadata
    except Exception as e:
        print(f"Failed to process URL: {url}, Error: {e}")

# Step 3: Save extracted content to JSONL format
output_file = "gut_health_articles_clean.jsonl"
with open(output_file, "w") as f:
    for doc in docs:
        json.dump({"url": doc.metadata.get("source", ""), "content": doc.page_content}, f)
        f.write("\n")

print(f"Content successfully saved to '{output_file}'")