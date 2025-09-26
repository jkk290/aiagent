import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_functions import available_functions
from functions.call_function import call_function
from config import MAX_ITERS

def aiagent(args):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    prompt = args[1]
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
   
    for i in range(MAX_ITERS):
        try:
            # print(f"Messages for prompt: {messages}")
            response = client.models.generate_content(
                model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),)

            # print(f"\n response candidates: {response.candidates}")

            if not response.function_calls and response.text:
                print(response.text)
                break
                
            for candidate in response.candidates:
                    # print(f"\n Candidate content: {candidate.content}")
                    messages.append(candidate.content)

            for function_call_part in response.function_calls:
                verbose = True
                fn_result = call_function(function_call_part, verbose)

                # print(f"\n fn result: {fn_result}")

                if not fn_result.parts[0].function_response.response:
                    raise Exception("called function didn't return a response")
                
                if verbose:
                    print(f"-> {fn_result.parts[0].function_response.response}")                

                messages.append(fn_result)

            if "--verbose" in args:   
                print(f"User prompt: {prompt}")     
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            
        except Exception as e:
            print(f"Error: {e}")

    

def main():
    if len(sys.argv) < 2:
        raise Exception("must enter a prompt, eg. python3 main.py \"why was 6 afraid of 7?\" [--verbose]")
        sys.exit(1)
    aiagent(sys.argv)

if __name__ == "__main__":
    main()
