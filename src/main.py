from src.llm_client import call_llm
from src.config import env

def main():
  try:
    prompt = input("Enter a prompt: ")
    print("sending request to LLM model --> "+env("GEMINI_MODEL"))
    response = call_llm(prompt)
    print(f"Response: {response}")
  except Exception as e:
    print(f"Error in main: {e}")


if __name__ == "__main__":
  main()