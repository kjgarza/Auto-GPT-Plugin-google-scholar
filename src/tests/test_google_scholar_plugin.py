import unittest
from unittest.mock import MagicMock, patch
from .google_scholar_plugin import GoogleScholarPlugin
from .google_scholar_search import GoogleScholarSearch

class TestGoogleScholarPlugin(unittest.TestCase):
    def test_execute(self):
        # Mock the search results from GoogleScholarSearch
        mock_results = [
            {
                'title': 'Test Title',
                'description': 'Test Abstract',
                'url': 'https://example.com',
                'doi': '10.1234/example'
            }
        ]

        with patch.object(GoogleScholarSearch, 'search', return_value=mock_results):
            google_scholar_plugin = GoogleScholarPlugin()
            keyword = 'test keyword'
            results = google_scholar_plugin.execute(keyword)

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
