
# Google Scholar Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A plugin for AutoGPT that searches Google Scholar and returns results in a JSON structure.

## Installation

To install in AutoGPT, copy the zipped repository into the `/plugins` folder in AutoGPT and add the name of the plugin in the .env file: 


```bash
ALLOWLISTED_PLUGINS=AutoGPTPluginGoogleScholar
```

## Usage

AutoGPT will use the command 'google_scholar_query' to find academic publications in google scholar.

```bash
17. message_agent: Message GPT Agent, args: "key": "<key>", "message": "<message>"
18. start_agent: Start GPT Agent, args: "name": "<name>", "task": "<short_task_desc>", "prompt": "<prompt>"
19. Task Complete (Shutdown): "task_complete", args: "reason": "<reason>"
20. google_scholar_query: "Search Academic Articles in Google Scholar", args: "keyword": "<keyword>", "limit": "<limit>"
```

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgements

- AutoGPT project
- Google Scholar
