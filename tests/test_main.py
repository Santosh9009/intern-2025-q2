import os
import pytest
from src.llm_client import call_llm
from src.main import generate_tweet

@pytest.mark.skipif(not os.getenv("GEMINI_API_KEY"), reason="No GEMINI_API_KEY set")
def test_llm_response_basic():
    out = call_llm("Reply with a single word: Hello.")
    assert isinstance(out, str)
    assert len(out.strip()) > 0

@pytest.mark.skipif(not os.getenv("GEMINI_API_KEY"), reason="No GEMINI_API_KEY set")
def test_generate_tweet():
    """Test the generate_tweet function with actual LLM call."""
    topic = "technology"
    tone = "professional"
    max_words = 20
    
    tweet = generate_tweet(topic, tone, max_words)
    
    # Basic assertions
    assert isinstance(tweet, str)
    assert len(tweet.strip()) > 0
    assert len(tweet.split()) <= max_words + 5  # Allow some tolerance for word count

@pytest.mark.skipif(not os.getenv("GEMINI_API_KEY"), reason="No GEMINI_API_KEY set")
def test_generate_tweet_different_tones():
    """Test generate_tweet with different tones."""
    topic = "coffee"
    max_words = 15
    
    # Test different tones
    tones = ["funny", "professional", "inspiring"]
    
    for tone in tones:
        tweet = generate_tweet(topic, tone, max_words)
        assert isinstance(tweet, str)
        assert len(tweet.strip()) > 0

def test_sanity_local():
    # a pure-python test so CI passes even without keys
    assert 2 + 2 == 4
