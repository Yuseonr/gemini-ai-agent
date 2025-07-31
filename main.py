import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_functions import available_functions, call_function
from prompt import system_promt

from config import MAX_ITTER

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def select_model(task_complexity="simple"):
    models = {
        
        "simple": "gemini-2.0-flash-001",  
        "complex": "gemini-2.5-flash"      
    }
    return models.get(task_complexity, models['simple'])

def main():
    RUN = True
    Itter = 0

    verbose = "--verbose" in sys.argv
 
    args = []
    for arg in sys.argv[1:] :
        if not '--' in arg :
            args.append(arg)
    
    # Input and models
    promt_arg = ' '.join(args)
    model_pick = select_model('simple')

    # No args handling
    if not args :
        print("\n--------------------------ALICE-------------------------\n")
        print('Usage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I become an software dev"\n')
        sys.exit(1)

    # assign role and setup for context memory
    messages = [
        types.Content(role='user', parts=[types.Part(text=promt_arg)]),
    ]

    if verbose :
        print("\n\nHello from gemini-ai-agent ALICE!\n")
        print(f'User prompt: {promt_arg}\nYour model : {model_pick}\nGenerating response ...\n\n')
    
    while RUN and Itter < MAX_ITTER:
        # Generating Response object
        response = client.models.generate_content(
            model=model_pick, 
            contents=messages,
            config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_promt,)
            )
        
        # Candidates
        for candidate in response.candidates :
            messages.append(candidate.content)

        # Metadata
        tokens = response.usage_metadata.prompt_token_count
        res_tokens = response.usage_metadata.candidates_token_count

        # Response object to text
        get_text_response = response.text
        # Response object to list of called function
        func_call = response.function_calls

        # spesify all the func you called
        result_called_function = []
        if func_call :
            for function in func_call :
                result = call_function(function,verbose)
                if (not result.parts or not result.parts[0].function_response) :
                    raise Exception("empty function call result")
                if verbose :
                    print(f"-> {result.parts[0].function_response.response}")

                result_called_function.append(result.parts[0].function_response.response)
                
                conv_func_response = types.Content(
                                        role="tool",
                                        parts=[
                                            types.Part.from_function_response(
                                                name=str(function),
                                                response={"result": result.parts[0].function_response.response},
                                                )
                                            ],
                                            )
                messages.append(conv_func_response)

            if not result_called_function : 
                raise Exception("no function responses generated.")
            
            Itter += 1
        else :
            print("Final Response : ")
            print(get_text_response)
            break
        
    if verbose :
        print(f'\nPrompt tokens: {tokens}')
        print(f'Response tokens: {res_tokens}')

if __name__ == "__main__":
        main()
