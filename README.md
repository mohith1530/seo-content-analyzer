# SEO Content Analyzer Tool

A web-based SEO Content Analyzer that evaluates webpages for SEO readiness and provides suggestions to improve search engine optimization.

---

## Live Application

https://seo-content-analyzer-7537.onrender.com

---

## GitHub Repository

https://github.com/mohith1530/seo-content-analyzer

---

# Project Overview

The SEO Content Analyzer is a web application that analyzes a webpage for SEO-related metrics. Users can enter a webpage URL and a target keyword. The application fetches the webpage content, evaluates various SEO factors, and generates a report with suggestions for improvement.

The system extracts important elements such as the page title, meta description, headings, keyword density, readability score, and image alt attributes. Based on these metrics, the tool calculates an SEO score and provides recommendations to improve search engine optimization.

---

# Tech Stack Chosen and Why

## Backend
- Python
- Flask
- BeautifulSoup
- Requests
- Textstat

## Frontend
- HTML
- CSS
- Jinja Templates

## Deployment
- Render

## Version Control
- Git
- GitHub

Python was chosen because it provides strong libraries for web scraping and text analysis. Flask was used as a lightweight web framework to quickly build the web application. BeautifulSoup was used to parse HTML content, while Requests was used to fetch webpage data. Textstat was used to calculate readability scores.

Render was used for deployment because it easily integrates with GitHub and supports Python web applications.

---

# AI Tools Used

AI tools such as **ChatGPT** were used during development to assist with:

- Understanding project requirements
- Structuring the Flask application
- Implementing SEO analysis logic
- Fixing deployment issues
- Writing documentation and README content

AI tools helped accelerate development and troubleshoot problems efficiently.

---

# Trade-offs and Prioritization

Due to the limited development timeline (2–3 days), the focus was placed on implementing the core functionality of the SEO analyzer.

Priority was given to:
- Core SEO analysis features
- Clean user interface
- Reliable deployment

Some advanced features such as text input analysis, advanced keyword analysis, and enhanced UI design were not included in order to ensure the main functionality was completed successfully.

---

# Features

- Analyze webpages using a URL
- Keyword density calculation
- Word count analysis
- Title extraction
- Meta description detection
- Heading structure analysis (H1 / H2)
- Image ALT tag detection
- Readability score calculation
- SEO score generation
- SEO improvement suggestions

---

# Example Input

URL:
https://www.bbc.com/news

Keyword:
news

---

# Possible Improvements

If more development time were available, the following features could be added:

- Analyze pasted text content in addition to URLs
- Improve UI using Bootstrap or modern frontend frameworks
- Highlight keywords in analyzed content
- Export SEO reports as PDF
- Add additional SEO metrics such as internal links or page speed analysis

---

# Known Limitations

- Some websites may block scraping requests
- JavaScript-generated content may not be fully captured
- SEO analysis is limited to HTML content
- On the free Render hosting plan, the application may go to sleep after inactivity, which can delay the first request

---

# Author

P.V.S.S Mohith

GitHub:  
https://github.com/mohith1530
