from functions.get_files_info import get_files_info

try_dir = [('calculator','.'), ("calculator", "pkg"),("calculator", "/bin"),("calculator", "../")]

for work_dir, directory in try_dir :
    print(f"Result for '{directory}' directory:")
    print(get_files_info(work_dir,directory))