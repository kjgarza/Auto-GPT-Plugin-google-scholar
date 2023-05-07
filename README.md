
# Google Scholar Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A plugin for AutoGPT that searches Google Scholar and returns results in a JSON structure.

## Installation

To install in AutoGPT, copy the zipped repository into the `/plugins` folder in AutoGPT and add the name of the plugin in the .env file: 


```bash
ALLOWLISTED_PLUGINS=AutoGPTPluginGoogleScholar
```

You will also need to run the [Run the dependency install script for plugins](https://github.com/Significant-Gravitas/Auto-GPT-Plugins#installation)

```bash
python -m autogpt --install-plugin-deps
```


## Usage

AutoGPT will use the command 'google_scholar_query' to find academic publications in google scholar. The following ai_settings.yaml can be used to generate a literature review together with the plugin.

```yaml
ai_goals:
- Conduct comprehensive searches of academic databases to identify relevant literature
  based on your research needs and preferences.
- Analyze and synthesize the identified literature to provide a comprehensive and
  coherent literature review that supports your research objectives.
- Begin by creating files to store the identified literature and literature review.
- Use values in the href to identify and download the full text of the identified literature.
- Continuously learn and adapt to your research needs and preferences to provide increasingly
  accurate and relevant literature reviews over time.
- Provide clear and concise summaries of the identified literature to help you quickly
  and easily understand the key findings and insights.
ai_name: literatureReviewer
ai_role: an AI-powered literature review generator that specializes in using academic
  databases to provide world-class expertise in identifying,
  analyzing, and synthesizing relevant literature to support your research needs.
  Will always start by asking the topic of the literature review.
api_budget: 0.0
```




## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgements

- AutoGPT project
- Google Scholar
