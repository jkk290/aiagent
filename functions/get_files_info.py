import os
from google import genai
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with thier sizes, constrained to the  working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(os.path.join(working_directory, directory))

    if not (abs_full == abs_work or abs_full.startswith(abs_work + os.path.sep)):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    
    if os.path.isdir(abs_full) == False:
        return f"Error: \"{directory}\" is not a directory"
    
    dir_contents = os.listdir(abs_full)
    dir_info = []

    for content in dir_contents:
        entry_path = os.path.join(abs_full, content)
        try:
            dir_info.append(f"- {content}: file_size={os.path.getsize(entry_path)} bytes, is_dir={os.path.isdir(entry_path)}")
        except Exception as e:
            return f"Error: {e}"
    
    return "\n".join(dir_info)