from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def results(label, w_dir, dir):
    print(f"Result for {label}:")
    result = get_file_content(w_dir, dir)
    formatted_result = "\n".join(f" {line}" for line in result.splitlines())
    print(formatted_result)

# results("lorem file", "calculator", "lorem.txt")
results("main.py", "calculator", "main.py")
results("pkg/calculator.py", "calculator", "pkg/calculator.py")
results("'/bin/cat' directory", "calculator", "/bin/cat")
results("pkg/does_not_exists.py' directory", "calculator", "pkg/does_not_exists.py")