import os
from config import file_char_limit

def get_file_content(working_directory, file_path):

    try:
        abs_work = os.path.abspath(working_directory)
        abs_full = os.path.abspath(os.path.join(working_directory, file_path))

        if not (abs_full == abs_work or abs_full.startswith(abs_work + os.path.sep)):
            return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
        
        if not (os.path.isfile(abs_full)):
            return f"Error: File not found or is not a regular file: \"{file_path}\""

        with open(abs_full, "r") as f:
            file_content_string = f.read(file_char_limit)
        
        if len(file_content_string) == file_char_limit:
            file_content_string_truncated = file_content_string + f"\n[...File \"{file_path}\" truncated at 10000 characters]"
        
            return file_content_string_truncated
        
        return file_content_string
    
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of a file as a string. If the character count is over 10,000, the content gets truncated at 10,000 characters. A footer note is appended to inform about the truncation",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to get contents from. Include subfolder with filename if file is in a subfolder(s) of the working directory. Example \"pkg/file.txt\"",
            ),
        },
    ),
)
    
