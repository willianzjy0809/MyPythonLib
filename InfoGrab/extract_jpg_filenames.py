#这段代码的主要功能是遍历指定文件夹中的所有以 '.jpg' 结尾的文件，提取文件名（不包含扩展名），并将这些文件名以逗号分隔的形式写入一个名为 'file_names.txt' 的文本文件中。以下是代码的概括

import os

folder_path = r'Z:\艺术收藏\000'  # 替换为您的文件夹路径
jpg_files = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

output_file = 'file_names.txt'

with open(output_file, 'w', encoding='utf-8') as file:
    for i, jpg_file in enumerate(jpg_files, start=1):
        file.write(f'"{jpg_file}",')
