import os

# 指定包含要修改文件的文件夹路径
folder_path = r'V:\MEDIA\国产类电影'  # 使用原始字符串以处理路径中的反斜杠

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    # 检查文件名是否包含 (年份) 格式
    if '(' in filename and ')' in filename:
        # 提取年份和文件名部分
        base_name, ext = os.path.splitext(filename)  # 分离文件名和扩展名
        name, year = base_name.split('(')
        year = year.split(')')[0]
        name = name.strip()  # 去除额外空格

        # 创建新文件名
        new_filename = f'{year.strip()} - {name.strip()}{ext}'

        # 构建新文件路径
        new_file_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(os.path.join(folder_path, filename), new_file_path)
        print(f'Renamed: {filename} to {new_filename}')
