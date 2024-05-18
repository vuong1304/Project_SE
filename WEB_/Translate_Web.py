import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# def translate_text(english_text):
#     translator = Translator()
#     if isinstance(translate_text, str):
#         translation = translator.translate(english_text, src='en', dest='vi')
#         return translation.text

# # Function to scrape data from a webpage
# def scrape_webpage(url):
#     # Send a GET request to the URL
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content of the page
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Extract the information you need from the HTML
#         # For example, let's extract the text from all <p> tags
#         paragraphs = soup.find_all('p')
#         text = '\n'.join([translate_text(p.get_text()) for p in paragraphs])
        
#         return text
#     else:
#         print("Failed to retrieve the webpage. Status code:", response.status_code)
#         return None

def translate_text(english_text):
    translator = Translator()
    try:
        # Ensure input is a string
        if isinstance(english_text, str) and english_text.strip():
            translation = translator.translate(english_text, src='en', dest='vi')
            return translation.text
        else:
            return ''
    except Exception as e:
        print(f"Translation error: {e}")
        return ''

# Function to scrape data from a webpage
def scrape_webpage(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the information you need from the HTML
        paragraphs = soup.find_all('p')
        translated_paragraphs = []

        for p in paragraphs:
            paragraph_text = p.get_text().strip()
            if paragraph_text:
                translated_text = translate_text(paragraph_text)
                if translated_text:
                    translated_paragraphs.append(translated_text)

        text = '\n'.join(translated_paragraphs)
        return text
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

# URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Cristiano_Ronaldo'  # Replace this with the URL you want to scrape

# Scrape the webpage
webpage_content = scrape_webpage(url)

if webpage_content:
    # Print the scraped content
    print("Scraped content:\n", webpage_content)
else:
    print("Scraping failed.")
