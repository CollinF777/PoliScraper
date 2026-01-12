import re
from config import KEYWORDS
from urllib.parse import urlparse

# Count political keywords in text by category
def analyze_keywords(text):
    scores = {"left": 0, "center": 0, "right": 0}
    found_keywords = {"left": [], "center": [], "right": []}
    for category, keywords in KEYWORDS.items():
        for keyword in keywords:
            """
            This is a regex pattern that is meant to match the keyword as the entire word
            The \b is a word boundary so the word cant be matched inside other words
            re.escape(keyword) escapes special regex characters in the keyword
            """
            pattern = r'\b' + re.escape(keyword) + r'\b'
            count = len(re.findall(pattern, text))

            if count > 0:
                scores[category] += count
                found_keywords[category].append(keyword)
    return scores, found_keywords

# Calculate political bias scores from keyword count
def bias_score_calc(scores):
    total = sum(scores.values())
    if total == 0:
        return 0

    # We are using a -5 to +5 with -5 being left +5 being right
    bias = (scores["right"] - scores["left"]) / total * 5
    return bias

# Analyzes every scraped site
def analyze_all_sites(sdata):
    results = []

    for url, data in sdata.items():
        text = data["text"]
        bias_info = data["bias_info"]

        scores, keywords = analyze_keywords(text)
        calculated_bias_score = bias_score_calc(scores)

        # Extract the domain
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")

        results.append({
            "url": url,
            "name": domain,
            "known_bias": bias_info["bias"],
            "bias_rating": bias_info["rating"],
            "calculated_bias": calculated_bias_score,
            "reliability": bias_info["credibility"],
            "scores": scores,
            "keywords": keywords,
            "total_keywords": sum(scores.values()),
            "source": bias_info["source"]
        })
    return results

# Print everything to console
def print_results(results):
    print("-"*50)
    print("Analysis Results")
    print("-"*50)
    for result in results:
        bias_diff = result["calculated_bias"] - result["known_bias"]
        agreement = "Close" if abs(bias_diff) < 1.0 else "Different"

        print(f"\\n{result['name']}")
        print(f"Known Bias: {result["known_bias"]} ({result["bias_rating"]} - via {result["source"]}")
        print(f"Calculated Bias: {result['calculated_bias']}")
        print(f"Difference: {agreement}")
        print(f"Credibility: {result['reliability']}/10")
        print(f"Keyword counts - Left: {result["scores"]["left"]}",
              f"Center: {result['scores']['center']}",
              f"Right: {result['scores']['right']}")