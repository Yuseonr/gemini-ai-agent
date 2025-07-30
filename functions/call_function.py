# 30 / Jul / 2025
# handles abstraction of calling function

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file 
from functions.run_python_file import run_python_file
from google.genai import types

def call_function(function_call_part, verbose=False):

    # Dictionary mapping function names to actual functions
    available_functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file
    }
    
    function_name = function_call_part.name
    
    # Print function call info based on verbose flag
    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}({function_call_part.args})")
    
    # Check if function name is valid
    if function_name not in available_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Get the function and prepare arguments
    function_to_call = available_functions[function_name]
    function_args = dict(function_call_part.args)
    
    # Add working_directory to the arguments
    function_args["working_directory"] = "./calculator"
    
    try:
        # Call the function with the arguments
        function_result = function_to_call(**function_args)
        
        # Return successful result
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    
    except Exception as e:
        # Handle any errors during function execution
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Function execution failed: {str(e)}"},
                )
            ],
        )