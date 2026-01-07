# Keywords we are using to find bias
KEYWORDS = {
    "left": [
        "progressive", "liberal", "pro-choice", "medicare for all", "wealth tax",
        "climate justice", "racial justice", "equity", "union rights", "living wage",
        "gun control", "environmental regulation", "public healthcare", "social programs",
        "immigrant rights", "reproductive rights", "communism", "socialism"
    ],

    "center": [
        "bipartisan", "moderate", "centrist", "pragmatic", "compromise",
        "fiscal moderation", "middle ground", "incremental reform",
        "independent", "nonpartisan", "evidence-based policy",
        "both sides"
    ],

    "right": [
        "conservative", "traditional values", "pro-life", "trad", "conservatism"
        "free market", "limited government", "tax cuts", "deregulation",
        "second amendment", "border security", "law and order", "patriotism",
        "family values", "strong defense", "fiscal conservatism", "america first"
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
MAX_CHARS = 10000
REQUEST_TIMEOUT = 10
USER_AGENT = 'PoliScraper/1.0 (+https://github.com/CollinF777/PoliScraper)'