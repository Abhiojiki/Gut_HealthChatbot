from usp.tree import sitemap_tree_for_homepage
import pandas as pd
import re
import requests
import csv
from bs4 import BeautifulSoup


from bs4 import BeautifulSoup
# 

# Create a new class Mayo to encapsulate functionality
class Mayo:
    def __init__(self, homepage_url: str):
        self.homepage_url = homepage_url

    # def filter_callback(self, url: str, recursion_level: int, parent_urls: set[str]) -> bool:
    #     excluded_languages = ['es', 'pt', 'fr', 'it', 'de', 'zh', 'ja', 'ko', 'ru', 'ar', 'zh-hans']
    #     return not any(f'/{lang}/' in url for lang in excluded_languages)

    def fetch_sitemap(self) -> pd.DataFrame:
        tree = sitemap_tree_for_homepage(
            self.homepage_url,
            # recurse_callback=self.filter_callback,
        )

        # Extract all pages from the sitemap
        data = [page.to_dict() for page in tree.all_pages()]

        # Filter URLs manually to exclude language-specific paths
        excluded_languages = ['es', 'pt', 'fr', 'it', 'de', 'zh', 'ja', 'ko', 'ru', 'ar', 'zh-hans']
        filtered_data = [page for page in data if not any(f'/{lang}/' in page['url'] for lang in excluded_languages)]

        # Convert filtered data to a DataFrame
        pages_df = pd.DataFrame(pd.json_normalize(filtered_data))
        return pages_df

    def filter_by_keywords(self, pages_df: pd.DataFrame, keywords: list[str]) -> pd.DataFrame:
        return pages_df[pages_df['url'].str.contains('|'.join(keywords), case=False)]

    def save_to_csv(self, pages_df: pd.DataFrame, filename: str) -> None:
        pages_df.to_csv(filename, index=False)


class Healthline:
    def __init__(self, homepage_url: str):
        self.homepage_url = homepage_url
        
    def filter_callback(self,url:str, recursion_level:int,parent_urls:set[str])->bool:
        excluded_languages = ['es', 'pt', 'fr', 'it', 'de', 'zh', 'ja', 'ko', 'ru', 'ar', 'zh-hans']
        return not any(f'/{lang}/' in url for lang in excluded_languages)

    def fetch_sitemap(self) -> pd.DataFrame:
        tree = sitemap_tree_for_homepage(
            self.homepage_url,
            recurse_callback=self.filter_callback,
        )
        
        
        # Extract all pages from the sitemap
        data = [page.to_dict() for page in tree.all_pages()]
        #filter urls manually to exclude language-specific paths
        excluded_languages = ['es', 'pt', 'fr', 'it', 'de', 'zh', 'ja', 'ko', 'ru', 'ar', 'zh-hans']
        filtered_data = [page for page in data if not any(f'/{lang}/' in page['url'] for lang in excluded_languages)]
        pages_df = pd.DataFrame(pd.json_normalize(filtered_data))
        return pages_df
    
    
    def filter_by_keywords(self, pages_df: pd.DataFrame, keywords: list[str]) -> pd.DataFrame:
        return pages_df[pages_df['url'].str.contains('|'.join(keywords), case=False)]

    def save_to_csv(self, pages_df: pd.DataFrame, filename: str) -> None:
        pages_df.to_csv(filename, index=False)
        

class Webmd:
    def __init__(self, base_url: str, pages: int):
        self.base_url = base_url
        self.pages = pages

    def is_digestive_health_article(self, url: str) -> bool:
        # Matches URLs like /digestive-health/20250825/article-title
        return bool(re.search(r'/digestive-health/\d{8}/', url))

    def fetch_articles(self) -> set:
        article_urls = set()

        for pg in range(1, self.pages + 1):
            page_url = self.base_url if pg == 1 else f"{self.base_url}?pg={pg}"
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, "html.parser")

            for a in soup.find_all("a", href=True):
                href = a.attrs.get("href")
                # Normalize relative URLs
                if href and isinstance(href, str) and href.startswith("/"):
                    href = "https://blogs.webmd.com" + href
                if href and isinstance(href, str) and self.is_digestive_health_article(href):
                    article_urls.add(href)

        return article_urls

    def save_to_csv(self, article_urls: set, filename: str) -> None:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["url"])
            for url in sorted(article_urls):
                writer.writerow([url])
