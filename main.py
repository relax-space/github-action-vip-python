'''
写内容到文件: hello_github_ci.txt
'''
import os
import sys


def get_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.argv[0])
    elif __file__:
        return os.path.dirname(__file__)


def main():
    path = get_dir()
    text = 'hello_github_ci.txt'
    file_path = os.path.join(path, text)
    with open(file_path, mode='w', encoding='utf8') as f:
        f.write(text)


if __name__ == '__main__':
    main()
