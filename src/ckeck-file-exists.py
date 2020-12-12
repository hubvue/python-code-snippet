# 检查文件是否存在

from pathlib import Path
import os

# 1.使用try/except块来检查文件是否存在（Python2+）


def readFileWithTryExcept(filePath: str):
    try:
        with open(filePath, 'r') as file:
            print('file', file)
    except FileNotFoundError:
        print('%s not exists' % (filePath))


# readFileWithTryExcept('src/list-element-add.py')

# 2.使用os.path检查文件是否存在（Python2+）


def readFileWithOS(filePath: str):
    exists = os.path.isfile(filePath)
    if exists:
        with open(filePath) as file:
            print('file', file)
    else:
        print('%s not exists' % (filePath))


# readFileWithOS('src/list-element-add.py')

# 3.使用Path对象来检查文件是否存在（Python3.4+）

def readFileWithPath(filePath: str):
    file = Path(filePath)
    if file.is_file():
        print('file', file.readlink())
    else:
        print('%s not exists' % (filePath))


readFileWithPath('src/list-element-add.py')
