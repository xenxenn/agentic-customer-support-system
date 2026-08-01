import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        #Remove unnecessary elements
        for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
            tag.decompose()

        #Try to find the main article content
        content = soup.find("article")

        if content is None:
            content = soup.find("main")

        if content is None:
            content = soup

        text = content.get_text(separator="\n", strip=True)

        #Limit extracted text to avoid very long inputs
        MAX_CHARACTERS = 5000
        if len(text) > MAX_CHARACTERS:
            text = text[:MAX_CHARACTERS]

        return text
    except requests.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    url = "https://cloud.google.com/blog"
    text = scrape_website(url)

    print(text[:1000])