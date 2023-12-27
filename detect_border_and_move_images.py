#这段代码使用 Python 的 PIL 库来检测图片是否具有黑边，并将具有黑边的照片移动到指定的子文件夹中。

from PIL import Image
import os
import shutil

def has_black_border(image_path, threshold=10):
    # 打开图像
    img = Image.open(image_path)

    # 转换为RGB模式，以便处理
    img = img.convert('RGB')

    # 获取图像的大小
    width, height = img.size

    # 获取图像四个边界的像素值
    top_row = [img.getpixel((i, 0)) for i in range(width)]
    bottom_row = [img.getpixel((i, height - 1)) for i in range(width)]
    left_column = [img.getpixel((0, j)) for j in range(height)]
    right_column = [img.getpixel((width - 1, j)) for j in range(height)]

    # 计算四个边界的平均像素值
    avg_top = sum(sum(color) for color in top_row) / len(top_row)
    avg_bottom = sum(sum(color) for color in bottom_row) / len(bottom_row)
    avg_left = sum(sum(color) for color in left_column) / len(left_column)
    avg_right = sum(sum(color) for color in right_column) / len(right_column)

    print(avg_top, avg_bottom, avg_left, avg_right)
    # 判断是否有黑边
    return (
        (avg_top < threshold and
        avg_bottom < threshold) or
        (avg_left < threshold and
        avg_right < threshold)
    )

def find_photos_with_black_border_and_move(folder_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    photos_with_black_border = []

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否是图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # 构建完整的文件路径
            image_path = os.path.join(folder_path, filename)

            # 判断是否有黑边
            if has_black_border(image_path):
                photos_with_black_border.append(image_path)

    # 移动文件到子文件夹
    for file_path in photos_with_black_border:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)

        # 使用shutil.move进行移动
        shutil.move(file_path, destination_path)
        print(f"Moved {file_name} to {destination_folder}")

    return photos_with_black_border

# 替换成你的照片文件夹路径
folder_path = r'C:\Users\willian.zhou\Downloads\test123'

# 目标子文件夹路径
destination_folder = os.path.join(folder_path, '123')

# 获取带有黑边的照片列表并移动到子文件夹
result = find_photos_with_black_border_and_move(folder_path, destination_folder)

# 打印结果
for photo_path in result:
    print(photo_path)
