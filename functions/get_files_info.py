import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    # print(f"creating full path...{full_path}")
    if full_path.startswith(working_directory) == False:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    
    if os.path.isdir(directory) == False:
        return f"Error: \"{directory}\" is not a directory"
    
    dir_contents = os.listdir(full_path)
    # print(f"got directory contents...{dir_contents}")
    dir_info = []
    for content in dir_contents:
        # print(f"checking content...{content}")
        try:
            dir_info.append(f"- {content}: file_size={os.path.getsize(content)} bytes, is_dir={os.path.isdir(content)}")
        except Exception as e:
            return f"Error: {e}"
        # print(f"dir_info updated...{dir_info}")    
    
    return "\n".join(dir_info)