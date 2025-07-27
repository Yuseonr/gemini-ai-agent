import os
import sys
from dotenv import load_dotenv
from google import genai

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

    # Input and models
    promt_arg = sys.argv[1]
    model_pick = select_model('simple')

    
    print("\n\nHello from gemini-ai-agent!\n")
    print(f'Your promt : {promt_arg}\nYour model : {model_pick}\nGenerating response ...\n\n')
    
    response = client.models.generate_content(
        model=model_pick, contents=promt_arg
    )
    
    tokens = response.usage_metadata.prompt_token_count
    res_tokens = response.usage_metadata.candidates_token_count
    get_text_response = response.text

    print(get_text_response)
    print(f'\nPrompt tokens: {tokens}')
    print(f'Response tokens: {res_tokens}')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else :
        print(f'main.py accepts 1 Args but {len(sys.argv) - 1} are given!')
        sys.exit(1)
