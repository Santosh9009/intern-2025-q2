from google import genai
from typing import Optional
from src.config import env

def call_llm(prompt: str, model: Optional[str] = None, timeout: int = 30) -> str:
    """
    Minimal LLM caller using Google's Generative AI (Gemini).
    """
    api_key = env("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY. Put it in a .env file (see .env.example).")

    model_name = model or env("GEMINI_MODEL", "gemini-2.5-flash")
    
    
    try:
        # Create a client
        client = genai.Client(api_key=api_key)
        
        # Generate content using the client
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        
        # Return the generated text from the response object
        return response.text
        
    except Exception as e:
        raise RuntimeError(f"Gemini API failed: {str(e)}")
