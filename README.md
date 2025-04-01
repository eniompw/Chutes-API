# Chutes-API

A simple Python client example for interacting with the [Chutes AI](https://chutes.ai) API.

## Description

This project demonstrates how to make API requests to the Chutes AI service to generate text completions using large language models (LLMs) like DeepSeek V3. Use this as a starting point for integrating Chutes AI capabilities into your Python applications.

## Prerequisites

- Python 3.6+
- `requests` library
- A Chutes AI API token

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Chutes-API.git
   cd Chutes-API
   ```

2. Install the required dependencies:
   ```bash
   pip install requests
   ```

3. Set up your API token as an environment variable:
   ```bash
   export CHUTES_API_TOKEN=cpk_...
   ```

## Usage

The example script `rest.py` demonstrates how to make a basic API request:

```python
import requests
import os

API_TOKEN = os.getenv("CHUTES_API_TOKEN")
API_URL = "https://llm.chutes.ai/v1/chat/completions"

# Make sure your API token is set
if not API_TOKEN:
    print("Error: CHUTES_API_TOKEN environment variable not set.")
else:
    # Sample request payload
    payload = {
        "model": "deepseek-ai/DeepSeek-V3-Base",
        "messages": [{"role": "user", "content": "What is the capital of France?"}],
        "max_tokens": 32
    }
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        print(response.json()["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Run the example:

```bash
python rest.py
```

## Customization

You can customize your API requests by modifying the payload:

- Change the `model` to use different AI models available through Chutes AI
- Update the `messages` array with different prompts
- Adjust parameters like `max_tokens`, `temperature`, etc.

## API Resources

- [Chutes AI Dashboard](https://chutes.ai/app)
- [API Documentation](https://chutes.ai/docs) (if available)

## License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.

## Support

For issues with the API itself, contact Chutes AI support.
For issues with this example code, please open an issue in the repository.
