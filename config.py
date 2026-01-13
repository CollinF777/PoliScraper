# Keywords we are using to find bias
KEYWORDS = {
    "left": [
        "progressive", "liberal", "left-wing", "democratic socialist",
        "social democracy", "anti-capitalist",
        "racial justice", "social justice", "equity", "inclusion",
        "systemic racism", "institutional racism",
        "civil rights", "voting rights", "voting access",
        "restorative justice",
        "lgbtq rights", "lgbtq+", "transgender rights", "gender affirming care",
        "nonbinary", "gender identity", "gender expression",
        "marriage equality", "pride",
        "abortion rights", "reproductive rights", "reproductive healthcare",
        "planned parenthood", "bodily autonomy",
        "climate change", "climate crisis", "climate justice",
        "environmental justice", "carbon emissions", "net zero",
        "renewable energy", "clean energy",
        "green new deal", "sustainability",
        "wealth tax", "billionaire tax", "corporate tax",
        "economic inequality", "income inequality",
        "minimum wage", "living wage",
        "student loan forgiveness", "debt relief",
        "universal basic income",
        "universal healthcare", "medicare for all",
        "public option", "healthcare access",
        "unions", "labor rights", "collective bargaining",
        "workers' rights", "strike", "fair wages",
        "immigration reform", "pathway to citizenship",
        "dreamers", "daca", "asylum seekers",
        "humane border policy",
        "police reform", "defund the police", "abolish police",
        "criminal justice reform", "mass incarceration",
        "human rights", "multilateralism", "diplomacy first"
    ],
    "center": [
        "moderate", "centrist", "middle ground",
        "independent voter", "swing voter",
        "bipartisan", "cross-party", "compromise",
        "consensus", "pragmatic approach",
        "balanced approach", "common sense",
        "evidence-based policy", "incremental reform",
        "fiscal responsibility", "measured response",
        "reasonable solution",
        "both sides", "across the aisle",
        "no easy answers", "nuanced debate"
    ],
    "right": [
        "conservative", "right-wing", "traditional values",
        "constitutional conservative", "limited government",
        "pro-life", "unborn child", "sanctity of life",
        "parental rights", "family values",
        "religious freedom", "faith-based",
        "anti-woke", "woke agenda",
        "second amendment", "gun rights",
        "constitutional carry",
        "law and order", "back the blue",
        "tough on crime",
        "border security", "secure the border",
        "illegal immigration", "illegal aliens",
        "border wall", "mass deportation",
        "free market", "capitalism",
        "deregulation", "cut regulations",
        "tax cuts", "lower taxes",
        "small government",
        "school choice", "charter schools",
        "critical race theory", "crt",
        "parental control in schools",
        "america first", "national sovereignty",
        "patriot", "patriotism",
        "strong military", "defense spending",
        "election integrity", "voter fraud",
        "secure elections"
    ]
}

# Websites that we will be using for our analysis
WEBSITES = [
    'https://www.npr.org',
    'https://www.bbc.com',
    'https://www.reuters.com',
    'https://www.foxnews.com',
    'https://www.cnn.com',
    'https://www.wsj.com',
    'https://www.nytimes.com',
    'https://www.washingtonpost.com',
    'https://www.breitbart.com',
    'https://www.huffpost.com',
    'https://www.thehill.com',
    'https://www.politico.com',
    'https://www.apnews.com',
    'https://www.usatoday.com',
    'https://www.nypost.com',
    'https://www.theguardian.com',
    'https://www.cbsnews.com',
    'https://www.nbcnews.com',
    'https://www.abcnews.go.com'
]

"""
To take note of sites already viewed as biased we will
take the bias rating from ALlSides and scale them as needed
-2 will represent left while +2 will be representing the right
as such, 0 will be considered non biased and a centrist source

Source:  https://www.allsides.com/media-bias/ratings
"""
RATINGS = {
    'npr.org': {'bias': -1, 'rating': 'Lean Left'},
    'bbc.com': {'bias': 0, 'rating': 'Center'},
    'reuters.com': {'bias': 0, 'rating': 'Center'},
    'foxnews.com': {'bias': 2, 'rating': 'Right'},
    'cnn.com': {'bias': -1, 'rating': 'Lean Left'},
    'wsj.com': {'bias': 0, 'rating': 'Center'},
    'nytimes.com': {'bias': -1, 'rating': 'Lean Left'},
    'washingtonpost.com': {'bias': -1, 'rating': 'Lean Left'},
    'breitbart.com': {'bias': 2, 'rating': 'Right'},
    'huffpost.com': {'bias': -2, 'rating': 'Left'},
    'thehill.com': {'bias': 0, 'rating': 'Center'},
    'politico.com': {'bias': -1, 'rating': 'Lean Left'},
    'apnews.com': {'bias': 0, 'rating': 'Center'},
    'usatoday.com': {'bias': 0, 'rating': 'Center'},
    'nypost.com': {'bias': 1, 'rating': 'Lean Right'},
    'theguardian.com': {'bias': -1, 'rating': 'Lean Left'},
    'cbsnews.com': {'bias': -1, 'rating': 'Lean Left'},
    'nbcnews.com': {'bias': -1, 'rating': 'Lean Left'},
    'abcnews.go.com': {'bias': -1, 'rating': 'Lean Left'},
}

"""
We will then create a set of data that will hold how each
of the websites credibility ratings from Media Bias Fact Check,
they rank on a scale from 0-10 so we will attach that to the 
websites

Source: https://mediabiasfactcheck.com
"""
MBFC_CREDIBILITY = {
    'npr.org': 9,
    'bbc.com': 9,
    'reuters.com': 10,
    'foxnews.com': 5,
    'cnn.com': 7,
    'wsj.com': 9,
    'nytimes.com': 8,
    'washingtonpost.com': 8,
    'breitbart.com': 4,
    'huffpost.com': 6,
    'thehill.com': 8,
    'politico.com': 8,
    'apnews.com': 10,
    'usatoday.com': 8,
    'nypost.com': 5,
    'theguardian.com': 7,
    'cbsnews.com': 8,
    'nbcnews.com': 8,
    'abcnews.go.com': 8,
}

# Some scraping settings for our program
MAX_CHARS = 100000
REQUEST_TIMEOUT = 10
USER_AGENT = 'PoliScraper/1.0 (+https://github.com/CollinF777/PoliScraper)'