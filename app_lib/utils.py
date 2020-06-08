import os


def convert_path(path: str):
    return path.replace('/', os.sep)


if __name__ == '__main__':
    print(convert_path(r"C:/Windows"))
