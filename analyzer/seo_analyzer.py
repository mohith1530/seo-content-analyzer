import requests
from bs4 import BeautifulSoup
import textstat

def analyze_seo(url, keyword):

    try:
        response = requests.get(
            url,
            verify=False,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        html = response.text
    except Exception as e:
        return {"Error": f"Unable to fetch URL: {e}"}

    soup = BeautifulSoup(html, "html.parser")

    # Extract text
    text = soup.get_text().lower()
    words = text.split()
    word_count = len(words)

    keyword_count = text.count(keyword.lower())

    keyword_density = (keyword_count / word_count) * 100 if word_count > 0 else 0

    # Title
    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_description = meta_desc["content"] if meta_desc and meta_desc.get("content") else "No meta description"

    # Headings
    h1_tags = len(soup.find_all("h1"))
    h2_tags = len(soup.find_all("h2"))

    # Images without alt
    images = soup.find_all("img")
    images_without_alt = len([img for img in images if not img.get("alt")])

    # Readability
    readability = textstat.flesch_reading_ease(text)

    score = 0
    suggestions = []

    # Word count
    if word_count > 300:
        score += 20
    else:
        suggestions.append("Increase content length (300+ words recommended)")

    # Keyword density
    if 1 <= keyword_density <= 3:
        score += 20
    else:
        suggestions.append("Keyword density should be between 1% and 3%")

    # Meta description
    if meta_description != "No meta description":
        score += 15
    else:
        suggestions.append("Add a meta description")

    # H1
    if h1_tags > 0:
        score += 15
    else:
        suggestions.append("Add at least one H1 heading")

    # H2
    if h2_tags > 0:
        score += 10
    else:
        suggestions.append("Add H2 subheadings")

    # Images ALT
    if images_without_alt == 0:
        score += 10
    else:
        suggestions.append("Add ALT text to images")

    # Readability
    if readability > 60:
        score += 10
    else:
        suggestions.append("Improve readability")

    result = {
        "SEO Score": score,
        "Title": title,
        "Word Count": word_count,
        "Keyword Count": keyword_count,
        "Keyword Density (%)": round(keyword_density, 2),
        "Meta Description": meta_description,
        "H1 Tags": h1_tags,
        "H2 Tags": h2_tags,
        "Images without ALT": images_without_alt,
        "Readability Score": round(readability, 2),
        "Suggestions": suggestions
    }

    return result