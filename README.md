# PoliScraper 

A Python-based tool for analyzing political bias in news media through keyword analysis and web scraping. PoliScraper compares calculated bias scores (derived from content analysis) against established ratings from AllSides and credibility scores from Media Bias/Fact Check.

## Features

- **Multi-Source Analysis**: Scrapes content from 19 major news outlets
- **Keyword-Based Bias Detection**: Uses comprehensive political keyword dictionaries
- **Visual Comparison**: Interactive Plotly charts comparing known vs. calculated bias
- **Credibility Scoring**: Integrates Media Bias/Fact Check credibility ratings
- **Ethical Scraping**: Respects robots.txt and implements rate limiting

## How It Works

1. **Web Scraping**: Collects homepage and article content from news websites
2. **Keyword Analysis**: Counts occurrences of left, center, and right-leaning keywords
3. **Bias Calculation**: Computes a bias score on a -5 (left) to +5 (right) scale
4. **Visualization**: Generates an interactive chart comparing results

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/CollinF777/PoliScraper.git
cd PoliScraper
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

**Required packages:**
- `requests` - HTTP library for web scraping
- `beautifulsoup4` - HTML parsing
- `plotly` - Interactive data visualization

## Usage

Run the main script:

```bash
python main.py
```

The program will:
1. Scrape content from configured news websites
2. Analyze political bias using keyword matching
3. Display results in the console
4. Generate an interactive HTML chart (`political_bias_chart.html`)
5. Automatically open the chart in your default browser

### Output

**Console Output:**
```
Analysis Results
--------------------------------------------------

npr.org
Known Bias: -1 (Lean Left - via AllSides and MBFC)
Calculated Bias: -0.85
Difference: Close
Credibility: 9/10
Keyword counts - Left: 45 Center: 12 Right: 23
```

**Visual Output:**
- Interactive HTML chart showing bias comparison
- Color-coded markers (blue = left, purple = center, red = right)
- Hover tooltips with detailed statistics

## Project Structure

```
PoliScraper/
├── main.py           # Entry point and orchestration
├── scraper.py        # Web scraping functionality
├── analyzer.py       # Bias calculation and keyword analysis
├── visualizer.py     # Chart generation
├── config.py         # Configuration, keywords, and ratings
├── requirements.txt  # Python dependencies
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Configuration

### Adding News Sources

Edit `config.py` to add new websites:

```python
WEBSITES = [
    'https://www.example-news.com',
]

RATINGS = {
    'example-news.com': {'bias': 0, 'rating': 'Center'},
}

MBFC_CREDIBILITY = {
    'example-news.com': 8,
}
```

### Customizing Keywords

Modify the `KEYWORDS` dictionary in `config.py`:

```python
KEYWORDS = {
    "left": ["progressive", "liberal", ...],
    "center": ["moderate", "bipartisan", ...],
    "right": ["conservative", "traditional", ...]
}
```

### Scraping Parameters

Adjust in `config.py`:

```python
MAX_CHARS = 100000        # Maximum characters per article
REQUEST_TIMEOUT = 10      # HTTP request timeout (seconds)
USER_AGENT = 'PoliScraper/1.0'  # User agent string
```

## Data Sources

### Bias Ratings
- **AllSides Media Bias Ratings**: Provides known bias classifications
  - Scale: Left (-2), Lean Left (-1), Center (0), Lean Right (+1), Right (+2)
  - Source: [allsides.com/media-bias/ratings](https://www.allsides.com/media-bias/ratings)

### Credibility Scores
- **Media Bias/Fact Check**: Provides credibility ratings
  - Scale: 0-10 (10 = highest credibility)
  - Source: [mediabiasfactcheck.com](https://mediabiasfactcheck.com)

## Analyzed News Outlets

The default configuration includes:

**Left-Leaning:**
- HuffPost
- The Guardian
- Washington Post
- The New York Times
- CNN, NPR, Politico, CBS, NBC, ABC

**Center:**
- Reuters, AP News, BBC, The Wall Street Journal
- The Hill, USA Today

**Right-Leaning:**
- New York Post
- Fox News
- Breitbart

## Methodology Notes

### Best Practices
This tool is intended for:
- Academic research and media literacy education
- Comparative media analysis
- Understanding keyword usage patterns

This tool should **not** be used as:
- The sole determinant of media bias
- A substitute for critical thinking
- A definitive measure of journalistic quality

## Ethical Considerations

- **Robots.txt Compliance**: Automatically checks and respects robots.txt rules
- **Rate Limiting**: Implements delays to avoid overwhelming servers
- **Attribution**: Properly credits data sources (AllSides, MBFC)
- **Transparency**: Open-source methodology available for scrutiny

## Troubleshooting

### Common Issues

**"No website could be scraped"**
- Check your internet connection
- Verify URLs in `config.py` are accessible
- Some sites may block automated scraping

**Import errors**
```bash
pip install --upgrade requests beautifulsoup4 plotly
```

**Low keyword counts**
- Increase `MAX_CHARS` in `config.py`
- Adjust `num_articles` parameter in scraping functions
- Verify articles are being found (check console output)

**Chart not displaying**
- Ensure Plotly is installed correctly
- Check if `political_bias_chart.html` was created
- Manually open the HTML file in a browser

## Disclaimer

This tool provides automated analysis based on keyword frequency and should not be considered a comprehensive assessment of media bias. Always critically evaluate news sources and consider multiple perspectives.

## Acknowledgments

- **AllSides** for media bias ratings
- **Media Bias/Fact Check** for credibility scores
- Built with Python, BeautifulSoup, and Plotly

## Contact

For questions or feedback, please open an issue on GitHub or contact Collin Fair (CollinF777).

---

**Note**: This tool is for educational and research purposes. Always respect website terms of service and copyright laws when scraping web content.
