def get_file_name(path: str) -> str:
    return path.split('\\')[-1].split('.')[0]


assert get_file_name(r"C:\development\inside\test-project_management\inside\myfile.txt") == "myfile"
assert get_file_name(r"C:\Users\ag.chelyadinskiy\PycharmProjects\pythonProject\config.ini") == "config"
