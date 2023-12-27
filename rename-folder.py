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
