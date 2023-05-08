from scholarly import scholarly
from scholarly import ProxyGenerator
from jinja2 import Template
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

        return formatted_results

    def _extract_data(self, result):
        bib = result.get('bib', {})
        data = {
            'title': bib.get('title', {}),
            'abstract': bib.get('abstract', {}).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip(),
            'url': result.get('eprint_url', ''),
            'doi': result.get('pub_url', '')
        }
        return data

    def _generate_proxy(self):
        pg = ProxyGenerator()
        pg.FreeProxies(timeout=1, wait_time=120)
        scholarly.use_proxy(pg)

    def _templated_response(self, results: list):

        jinja_string = """{{title}}:
        Total results: {{ results|length }}
        {% for result in results %}
        Title: {{ result.title }}
        Abstract: {{ result.abstract }}
        Url: {{ result.url }}
        Doi: {{ result.doi }}
        {% endfor %}

        These results include the following fields: title, Abstract, and url. You can use url to get more information about the result. For example, you can use url to get the result's full text and to reference the result in your own work.
        """

        template = Template(jinja_string)

        return template.render(title="Search Results", results=results)


    def _format_response(self, results: list, format: str):
        if format == 'json':
            return json.dumps(results, indent=4, ensure_ascii=False)
        elif format == 'text':
            return self._templated_response(results)
        else:
            return self._templated_response(results)