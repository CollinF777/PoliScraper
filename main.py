from config import WEBSITES
from scraper import scrape_mutiple
from analyzer import analyze_all_sites, print_results
from visualizer import create_bias_chart, display_chart, save_chart

def main():
    print("Using AllSides Media Bias Ratings + MBFC Credibility Scores")
    print("=" * 50)

    # Scrape websites and get bias ratings
    scraped_data = scrape_mutiple(WEBSITES)

    if not scraped_data:
        print("No website could be scraped, check url or network connection")
        return

    # Analyze bias
    results = analyze_all_sites(scraped_data)

    # Print results console
    print_results(results)

    # Generate and display visual
    fig = create_bias_chart(results)
    display_chart(fig)
    save_chart(fig)

if __name__ == "__main__":
    main()