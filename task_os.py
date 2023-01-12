import os
import sys


# 1
def get_files_from_folder(folder_path):
    return next(os.walk(folder_path))[2]


# 2
def get_current_dir():
    return os.getcwd()


# 3
def create_folder_in_current_dir(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


# 4
def join_folder_and_file(folder_path, filename):
    return os.path.join(folder_path, filename)


# 5
def load_stat_to_file(filepath):
    python_path = os.path.dirname(sys.executable)

    stat = {
        "files": 0,
        "folders": 0,
        "py_files": 0,
        "exe_files": 0,
    }

    for _, dirs, files in os.walk(python_path):
        stat["files"] += len(files)
        stat["folders"] += len(dirs)
        for file in files:
            if file.endswith(".py"):
                stat["py_files"] += 1
            elif file.endswith(".exe"):
                stat["exe_files"] += 1

    with open(filepath, "w") as fout:
        for key, val in stat.items():
            fout.write(f"{key}: {val}\n")
