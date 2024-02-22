'''
假设当前工作目录下有以下两个文件夹：

Folder1 (2020)
Folder2 (2015)
运行上述代码后，这两个文件夹将被重命名为：

2020 - Folder1
2015 - Folder2
这是因为代码遍历当前目录下的文件夹，对于包含括号且为文件夹的项，它会提取括号中的年份，去除额外空格，然后构建一个新的文件夹名，最后使用os.rename函数进行重命名。执行完成后，代码会输出类似以下的信息：

yaml
Copy code
Renamed folder: Folder1 (2020) to 2020 - Folder1
Renamed folder: Folder2 (2015) to 2015 - Folder2
这显示了每次重命名的操作，将原始文件夹名和新的文件夹名都显示出来。
'''

import os

# 获取当前工作目录
current_directory = os.getcwd()

for folder in os.listdir(current_directory):
    folder_full_path = os.path.join(current_directory, folder)
    if os.path.isdir(folder_full_path) and '(' in folder and ')' in folder:
        # 提取年份和文件夹名部分
        name, year = folder.split('(')
        year = year.split(')')[0]
        name = name.strip()  # 去除额外空格

        # 创建新文件夹名
        new_folder_name = f'{year.strip()} - {name.strip()}'

        # 构建新文件夹路径
        new_folder_full_path = os.path.join(current_directory, new_folder_name)

        # 重命名文件夹
        os.rename(folder_full_path, new_folder_full_path)
        print(f'Renamed folder: {folder} to {new_folder_name}')
