import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(os.path.join(working_directory, file_path))

    if not (abs_full == abs_work or abs_full.startswith(abs_work + os.path.sep)):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.exists(abs_full):
        return f"Error: File \"{file_path}\" not found"

    if not abs_full.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file"
    
    formatted_args = " ".join(args)

    try:
        executed = subprocess.run(["python3", abs_full, formatted_args], capture_output=True, text=True, timeout=30, cwd=abs_work)

        if executed.stdout == None or executed.stdout == "":
            return "No output produced"   
        
        formatted_output = f"STDOUT: {executed.stdout}\nSTDERR: {executed.stderr}"

        if not executed.returncode == 0:
            formatted_output_exit_code = formatted_output + f"\nProcess exited with code {executed.exitcode}"
            return formatted_output_exit_code

        return formatted_output
    except Exception as e:
        return f"Error: executing Python file: {e}"

