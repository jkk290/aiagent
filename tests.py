# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python_file import run_python_file

def results(w_dir, file_path, args=[]):
    # print(f"Result for {label}:")
    result = run_python_file(w_dir, file_path, args)
    formatted_result = "\n".join(f" {line}" for line in result.splitlines())
    print(formatted_result)

results("calculator", "main.py")
results("calculator", "main.py", ["3 + 5"])
results("calculator", "tests.py")
results("calculator", "../main.py")
results("calculator", "nonexistent.py")