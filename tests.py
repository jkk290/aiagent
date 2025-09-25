from functions.get_files_info import get_files_info

def results(label, w_dir, dir):
    print(f"Result for {label}:")
    result = get_files_info(w_dir, dir)
    formatted_result = "\n".join(f" {line}" for line in result.splitlines())
    print(formatted_result)

results("current directory", "calculator", ".")
results("'pkg' directory", "calculator", "pkg")
results("'/bin' directory", "calculator", "/bin")
results("'../' directory", "calculator", "../")