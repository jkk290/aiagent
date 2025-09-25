# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file

def results(w_dir, file_path, content):
    # print(f"Result for {label}:")
    result = write_file(w_dir, file_path, content)
    formatted_result = "\n".join(f" {line}" for line in result.splitlines())
    print(formatted_result)

results("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
results("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
results("calculator", "/tmp/temp.txt", "this should not be allowed")