import unittest
from unittest.mock import MagicMock, patch
from google_scholar_search import GoogleScholarSearch

class TestGoogleScholarSearch(unittest.TestCase):
    def test_search(self):
        # Mock the Google Scholar API response
        mock_response = [
            {
                'title': 'Test Title',
                'abstract': 'Test Abstract',
                'url': 'https://example.com',
                'doi': '10.1234/example'
            }
        ]

        with patch('scholarly.search_pubs', return_value=mock_response):
            google_scholar_search = GoogleScholarSearch()
            keyword = 'test keyword'
            results = google_scholar_search.search(keyword)

        expected_results = [
            {
                'title': 'Test Title',
                'description': 'Test Abstract',
                'url': 'https://example.com',
                'doi': '10.1234/example'
            }
        ]

        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
