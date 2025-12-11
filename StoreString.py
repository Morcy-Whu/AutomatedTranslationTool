# StoreString.py
import datetime
import os

now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d-%H-%M-%S")

# 默认存储路径（你可按需修改）
DEFAULT_PATH = (r"D:\Applications\Pycharm Project\MarianMT\Output\\") + filename + ".txt"


def store_string(text: str, path: str = None):
    """
    Store the given string into a text file.

    Args:
        text (str): The string to store.
        path (str, optional): The file path to write to.
                              If omitted, DEFAULT_PATH is used.
    """

    # 如果用户没有提供 path，则使用默认路径
    if path is None:
        path = DEFAULT_PATH
    else:
        path = path + "\\" + filename + ".txt"

    # 确保目标文件夹存在
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    # 写入文件
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"String successfully stored at: {path}")
