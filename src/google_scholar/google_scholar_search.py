from scholarly import scholarly

class GoogleScholarSearch:
    def search(self, keyword):
        search_results = scholarly.search_pubs(keyword)
        formatted_results = []

        for result in search_results:
            formatted_result = self._extract_data(result)
            formatted_results.append(formatted_result)

        return formatted_results

    def _extract_data(self, result):
        bib = result.get('bib', {})
        data = {
            'title': bib.get('title', {}),
            'description': bib.get('abstract', {}),
            'url': result.get('eprint_url', ''),
            'doi': result.get('pub_url', '')
        }
        return data
