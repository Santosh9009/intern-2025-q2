# Intern Assignment Q1: Hello LLM

This assignment demonstrates making secure LLM calls using Google's Generative AI (Gemini) API.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Gemini API Key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the API key

3. **Create .env file:**
   ```bash
   # Create .env file in the project root
   GEMINI_API_KEY=your_actual_api_key_here
   GEMINI_MODEL=gemini-1.5-flash
   ```

## Usage

Run the main script:
```bash
python -m src.main
```

# Test
Run the test script:
```bash
python -m pytest
```


## What it does

- Loads API key securely from `.env` file using `python-dotenv`
- Makes a request to Gemini API using `google-generativeai` library
- Prints the greeting response from the LLM

## Files

- `src/main.py` - Main script that calls the LLM
- `src/llm_client.py` - LLM client using Gemini API
- `src/config.py` - Configuration and environment variable loading
- `requirements.txt` - Python dependencies

## Available Gemini Models

- `gemini-1.5-flash` - Fast and efficient (default)
- `gemini-1.5-pro` - More capable but slower
- `gemini-1.0-pro` - Legacy model

## Security

✅ API key is stored in `.env` file (not committed to git)
✅ Uses official Google Generative AI Python client
✅ Secure API calls with proper error handling
