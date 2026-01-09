import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from config import MAX_CHARS, REQUEST_TIMEOUT, USER_AGENT, RATINGS, MBFC_CREDIBILITY
from urllib.robotparser import RobotFileParser

# Method to get the domain from a given url
def getDomain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace("www.","")
    return domain

# Checks for a robots.txt to file to make sure we can scrape
def can_scrape(url):
    try:
        parsed_url = urlparse(url)

        # Construct robots.txt URL, if you understand this ignore large comment
        """
        To construct a websites robots.txt URL you must combine a few things
        First you need the scheme which like http or https
        Then you need the netlock which is the domain with a subdomain like www.colliniscool.com
        After you add the path which is robots.txt
        """
        robots_url = parsed_url.scheme + "://" + parsed_url.netloc + "/robots.txt"

        # Create the robot parser
        robots_parser = RobotFileParser()
        robots_parser.set_url(robots_url)
        robots_parser.read()

        # Check if we are allowed to fetch the url, * is just so its generic
        can_fetch = robots_parser.can_fetch("*",url)

        if not can_fetch:
            print(f"Warning for {url}: robots.txt does not allow scraping")

        return can_fetch

    except Exception as e:
        print(f"No robots.txt for {url} proceeding as normal")
        return True
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

            # Check robots.txt for scraping permissions
            if not can_scrape(website):
                print(f"Skipping {website}: Robots.txt disallows scraping")
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