from src.llm_client import call_llm
from src.config import env

def generate_tweet(topic: str, tone: str, max_words: int) -> str:
    """
    Generate a tweet using LLM with prompt template and variables.
    
    This function demonstrates prompt engineering basics by:
    1. Using template variables to create dynamic prompts
    2. Formatting prompts with specific instructions and constraints
    3. Making the prompt parameterizable and reusable
    
    Args:
        topic (str): The topic to tweet about
        tone (str): The tone of the tweet (e.g., "funny", "professional", "inspiring")
        max_words (int): Maximum number of words in the tweet
    
    Returns:
        str: Generated tweet from the LLM
    """
    # PROMPT ENGINEERING: Format prompt template with variables
    # Template: "Write a {tone} tweet about {topic} in under {max_words} words."
    prompt = f"Write a {tone} tweet about {topic} in under {max_words} words."
    
    try:
        print(f"Sending request to LLM model --> {env('GEMINI_MODEL')}")
        print(f"Formatted Prompt: {prompt}")
        response = call_llm(prompt)
        return response.strip()
    except Exception as e:
        raise RuntimeError(f"Error generating tweet: {e}")

def main():
    try:
        # Demo the generate_tweet function
        print("=== Tweet Generator Demo ===\n")
        
        # Example 1: Funny tweet about AI
        print("Example 1: Funny tweet about AI")
        tweet1 = generate_tweet("artificial intelligence", "funny", 25)
        print(f"Generated Tweet: {tweet1}\n")
        
        # Example 2: Professional tweet about climate change
        print("Example 2: Professional tweet about climate change")
        tweet2 = generate_tweet("climate change", "professional", 30)
        print(f"Generated Tweet: {tweet2}\n")
        
        # Example 3: Inspiring tweet about learning
        print("Example 3: Inspiring tweet about learning")
        tweet3 = generate_tweet("learning new skills", "inspiring", 20)
        print(f"Generated Tweet: {tweet3}\n")
        
        # Interactive mode
        print("=== Interactive Mode ===")
        topic = input("Enter a topic: ")
        tone = input("Enter tone (e.g., funny, professional, inspiring): ")
        max_words = int(input("Enter max words: "))
        
        tweet = generate_tweet(topic, tone, max_words)
        print(f"\nGenerated Tweet: {tweet}")
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()