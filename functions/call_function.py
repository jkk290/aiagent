from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from config import WORKING_DIR

def call_function(function_call_part, verbose=False):
    valid_functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }

    fn_name = function_call_part.name
    fn_args = function_call_part.args

    if fn_name not in valid_functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=fn_name,
                    response={"error": f"Unknown function: {fn_name}"},
                )
            ],
        )
    
    if verbose:
        print(f"Calling function: {fn_name}({fn_args})")
    else:
        print(f" - Calling function: {fn_name}")
    
    executed = valid_functions[fn_name](WORKING_DIR, **fn_args)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=fn_name,
            response={"result": executed},
        )
    ],
)