# Intern Assignment Q2: Prompt Template with Variables

This assignment demonstrates prompt engineering basics by creating a tweet generator function that uses template variables to format prompts for LLM calls.

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
   GEMINI_MODEL=gemini-2.5-flash
   ```

## Usage

Run the main script:

```bash
# macOS / Linux
python3 -m src.main


# Windows (if python points to Python 3)
python -m src.main
```

## Test

```bash
# macOS / Linux
python3 -m pytest

# Windows
python -m pytest
```

## What it does

The main function `generate_tweet(topic, tone, max_words)` demonstrates prompt engineering by:

- Taking three parameters: `topic`, `tone`, and `max_words`
- Formatting a prompt template: `"Write a {tone} tweet about {topic} in under {max_words} words."`
- Sending the formatted prompt to the LLM
- Returning the generated tweet

## Sample Outputs

Here are 3 example outputs from the `generate_tweet` function:

### Example 1: Funny tweet about AI (25 words)
**Input:** `generate_tweet("artificial intelligence", "funny", 25)`  
**Output:** "AI is so smart it probably already knows what I'm going to tweet next. *nervously checks for robot uprising* 🤖 #AIHumor"

### Example 2: Professional tweet about climate change (30 words)
**Input:** `generate_tweet("climate change", "professional", 30)`  
**Output:** "Addressing climate change requires collective action from governments, businesses, and individuals. Together, we can build a sustainable future for generations to come. #ClimateAction #Sustainability"

### Example 3: Inspiring tweet about learning (20 words)
**Input:** `generate_tweet("learning new skills", "inspiring", 20)`  
**Output:** "Every expert was once a beginner. Embrace the journey of learning new skills—your future self will thank you! 🌟 #GrowthMindset"

## Function Signature

```python
def generate_tweet(topic: str, tone: str, max_words: int) -> str:
    """
    Generate a tweet using LLM with prompt template and variables.
    
    Args:
        topic (str): The topic to tweet about
        tone (str): The tone of the tweet (e.g., "funny", "professional", "inspiring")
        max_words (int): Maximum number of words in the tweet
    
    Returns:
        str: Generated tweet from the LLM
    """
```

## Files

- `src/main.py` - Main script with `generate_tweet()` function and demo
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

## Prompt Engineering Features

✅ **Template Variables:** Uses f-string formatting to inject variables into prompts  
✅ **Clear Instructions:** Specific format and constraints in the prompt  
✅ **Parameterized:** Flexible function that works with different topics, tones, and word limits
