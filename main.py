from Testing.test import Mayo, Webmd
from Testing.gut_keywords import gut_keywords
from Testing.test import Healthline


def main():
    # homepage_url = 'https://www.mayoclinic.org/diseases-conditions'
    # mayo = Mayo(homepage_url)

    # # Fetch sitemap and filter by keywords
    # pages_df = mayo.fetch_sitemap()
    # filtered_pages_df = mayo.filter_by_keywords(pages_df, gut_keywords)

    # # Save filtered pages to CSV
    # mayo.save_to_csv(filtered_pages_df, 'mayositemap-pages.csv')
    
    # homepage_url = 'https://www.healthline.com/inflammatory-bowel-disease'
    # healthline = Healthline(homepage_url)
    # # Fetch sitemap and filter by keywords
    # pages_df = healthline.fetch_sitemap()
    # filtered_pages_df = healthline.filter_by_keywords(pages_df, gut_keywords)

    # # Save filtered pages to CSV
    # healthline.save_to_csv(filtered_pages_df, 'healthlinesitemap-pages.csv')
    
    homepage_url = "https://www.webmd.com/"
    webmd = Webmd(homepage_url)
    # Fetch sitemap and filter by keywords
    pages_df = webmd.fetch_sitemap()
    filtered_pages_df = webmd.filter_by_keywords(pages_df, gut_keywords)

    # Save filtered pages to CSV
    webmd.save_to_csv(filtered_pages_df, 'webmdsitemap-pages.csv')

if __name__ == "__main__":
    main()
