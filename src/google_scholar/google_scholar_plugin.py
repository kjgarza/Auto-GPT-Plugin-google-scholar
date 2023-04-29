from .google_scholar_search import GoogleScholarSearch

class GoogleScholarPlugin:
    def __init__(self):
        self.google_scholar_search = GoogleScholarSearch()

    def execute(self, keyword: str):
        return self.google_scholar_search.search(keyword, limit=10)
