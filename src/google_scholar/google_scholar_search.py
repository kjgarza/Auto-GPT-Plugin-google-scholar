from scholarly import scholarly
from scholarly import ProxyGenerator


class GoogleScholarSearch:
    def search(self, keyword, limit=1):
        self._generate_proxy()
        search_results = scholarly.search_pubs(keyword)
        formatted_results = []
        counter = 0

        for result in search_results:
            if counter < limit:
                formatted_result = self._extract_data(result)
                formatted_results.append(formatted_result)
                counter += 1
            else:
                break

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

    def _generate_proxy(self):
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)