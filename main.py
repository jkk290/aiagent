import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def aiagent(args):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    prompt = args[1]
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
   
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages)   
    
    print(response.text)

    if "--verbose" in args:   
        print(f"User prompt: {prompt}")     
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def main():
    if len(sys.argv) < 2:
        raise Exception("must enter a prompt, eg. python3 main.py \"why was 6 afraid of 7?\" [--verbose]")
        sys.exit(1)
    aiagent(sys.argv)

if __name__ == "__main__":
    main()
