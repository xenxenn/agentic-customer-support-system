from scraper import scrape_website
from summarizer import summarize_text

url = "https://cloud.google.com/blog"

text = scrape_website(url)

summary = summarize_text(text)

print("\n===== SUMMARY =====\n")
print(summary)