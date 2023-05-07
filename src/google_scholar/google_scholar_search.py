from scholarly import scholarly
from scholarly import ProxyGenerator
import json

class GoogleScholarSearch:
    def search(self, keyword, limit):
        if self._generate_proxy() == False:
            return []

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

        return json.dumps(formatted_results, indent=4, ensure_ascii=False)

    def _extract_data(self, result):
        bib = result.get('bib', {})
        data = {
            'title': bib.get('title', {}),
            'description': bib.get('abstract', {}).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip(),
            'url': result.get('eprint_url', ''),
            'doi': result.get('pub_url', '')
        }
        return data

    def _generate_proxy(self):
        pg = ProxyGenerator()
        pg.FreeProxies(timeout=1, wait_time=120)
        scholarly.use_proxy(pg)