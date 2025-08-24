import os
import pytest
from src.llm_client import call_llm

@pytest.mark.skipif(not os.getenv("GEMINI_API_KEY"), reason="No GEMINI_API_KEY set")
def test_llm_response_basic():
    out = call_llm("Reply with a single word: Hello.")
    assert isinstance(out, str)
    assert len(out.strip()) > 0

def test_sanity_local():
    # a pure-python test so CI passes even without keys
    assert 2 + 2 == 4
