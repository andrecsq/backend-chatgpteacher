## Running
1. Create file `api_key.txt` with the OpenAI API Secret
2. Set up a python virtual environment with `python -m venv venv`
3. Load the virtual environment with `. venv/bin/activate` (Linux)
4. Install dependencies with `pip install -r requirements.txt`

5. Create a `.env` file in the root with at least a DEFAULT_MODEL key. Like this:
```
DEFAULT_MODEL=gpt-3.5-turbo
```
We recommend the model `gpt-4`


6. Run with `uvicorn app:app --reload`

Docs for OpenAI Python library: https://github.com/openai/openai-python
OpenAI API Documentation: https://platform.openai.com/ 