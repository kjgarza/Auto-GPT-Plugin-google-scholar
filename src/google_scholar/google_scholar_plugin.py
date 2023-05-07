from .google_scholar_search import GoogleScholarSearch

from . import AutoGPTPluginGoogleScholar

plugin = AutoGPTPluginGoogleScholar()

class GoogleScholarPlugin:
    def __init__(self):
        self.google_scholar_search = GoogleScholarSearch()

    def execute(self, keyword: str, limit: int = 10):
        """
        Search Academic Articles in Google Scholar
        Args:
                keyword (str): The keyword to search.
                limit (int): The limit of results.
        Returns:
                str: The resulting response in JSON format.
        """
        return self.google_scholar_search.search(keyword, int(limit))

