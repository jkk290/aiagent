import os
import subprocess
from google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_full == abs_work or abs_full.startswith(abs_work + os.path.sep)):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.exists(abs_full):
        return f"Error: File \"{file_path}\" not found"

    if not abs_full.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file"
    
    commands = ["python3", abs_full]

    if args:
        commands.extend(args)

    try:
        executed = subprocess.run(commands, capture_output=True, text=True, timeout=30, cwd=abs_work)

        if executed.stdout == None and executed.stderr == None:
            return "No output produced"   
        
        formatted_output = f"STDOUT: {executed.stdout}\nSTDERR: {executed.stderr}"

        if not executed.returncode == 0:
            formatted_output_exit_code = formatted_output + f"\nProcess exited with code {executed.returncode}"
            return formatted_output_exit_code

        return formatted_output
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file= types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file and returns the stdout, stderr, and exit code if not 0",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the python file to be ran. Include the subfolder with filename if file is in a subfolder(s) of the working directory. Example \"pkg/test.py\"",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Optional arguments to pass with the python file that will be ran. Example \"calculator.py\" \"5 + 3\""
            )
        },
    ),
)