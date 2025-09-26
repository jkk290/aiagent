import os

def write_file(working_directory, file_path, content):
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(os.path.join(working_directory, file_path))
    target_dir = os.path.dirname(abs_full)

    if not (abs_full == abs_work or abs_full.startswith(abs_work + os.path.sep)):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
    
    if (os.path.isdir(abs_full)):
        return f"Error: \"{file_path}\" is a directory, not a file"
    
    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        with open(abs_full, "w") as f:
            f.write(content)
        
        return f"Successfully wrote to \"{abs_full}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {e}"

schema_write_file= types.FunctionDeclaration(
    name="write_file",
    description="Write to new or overwrite file's content with the provided content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to be written to. Include the subfolder with filename if file is in a subfolder(s) of the working directory. Example \"pkg/test.txt\"",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text to be written to the given file"
            )
        },
    ),
)