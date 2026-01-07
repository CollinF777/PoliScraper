import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from config import MAX_CHARS, REQUEST_TIMEOUT, USER_AGENT, RATINGS, MBFC_CREDIBILITY

# Method to get the domain from a given url
def getDomain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace("www.","")
    return domain

# Gets the bias rating from Allsides and credibility from MBFC
def get_bias_cred(url):
    domain = getDomain(url)

    if domain in RATINGS:
        bias_rating = RATINGS[domain]
        """
        Default credibility is gonna set it to 5 if it cant be found
        the logic behind this is that 5 is right in the center so it
        shouldn't skew a website unrated by the MBFC either way
        """
        cred = MBFC_CREDIBILITY.get(domain, 5)

        return {
            'bias': bias_rating['bias'],
            'rating': bias_rating['rating'],
            'credibility': bias_rating['credibility'],
            'source': "AllSides and MBFC"
        }
    # If it cant be found then theres nothing to return
    return None

# Scrape a single website
def scrape1(url):
    try:
        # Here we have to set the User-Agent header to mimic a real browser or it might get blocked
        headers = {'User-Agent': USER_AGENT}
        # Make an HTTP GET request and check for error
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        """
        This removes specfic elements that we dont need to search
        script: No need to search any javascript elements as that just adds 
                website interaction
        style: How the website is stylized typically has little to do
               with a websites politics
        header/footer: Typically websites aren't using the header and footer
                       for meaningful content
        nav: The nav bar is typically just meant for user navigation, no need
             to look there
        """
        for element in soup(["script", "style", "header", "footer", "nav"]):
            element.decompose()

        # Extract and clean the text
        text = soup.get_text()
        # Replace whitespace with single spaces and remove leading/trailing whitespace also limit char
        text = re.sub(r'\\s+',' ', text).strip()[:MAX_CHARS]

        return text.lower()
    except Exception as e:
        print(f"Error in scrape1 on website {url}: {e}")
        return ""

# Scrape multiple websites
def scrape_mutiple(websites):
    scraped_data = {}

    for website in websites:
            print(f"Scraping {website}")

            bias_info = get_bias_cred(website)

            if bias_info is None:
                # No need to stop completely, just send a warning and move on
                print(f"Warning for {website}: No bias rating found")
                continue

            # Scrape text
            text = scrape1(website)

            if text:
                scraped_data[website] = {
                    'text': text,
                    'bias': bias_info
                }
                print(f"Rating found for {website}: {bias_info['rating']} Credibility: {bias_info['credibility']}/10")

            return scraped_data