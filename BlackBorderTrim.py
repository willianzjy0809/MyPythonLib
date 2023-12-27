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

def find_photos_with_black_border_and_crop(folder_path, destination_folder):
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
                # 打开图像
                img = Image.open(image_path)

                # 获取非黑边区域的矩形范围
                top, left, bottom, right = find_non_black_border_rect(img)

                # 裁剪图像
                img_cropped = img.crop((left, top, right, bottom))

                # 保存裁剪后的图像
                destination_path = os.path.join(destination_folder, filename)
                img_cropped.save(destination_path)

                print(f"Cropped and saved {filename} to {destination_folder}")

                photos_with_black_border.append(destination_path)

    return photos_with_black_border

def find_non_black_border_rect(img):
    # 获取图像的大小
    width, height = img.size

    # 获取图像四个边界的像素值
    top_row = [img.getpixel((i, 0)) for i in range(width)]
    bottom_row = [img.getpixel((i, height - 1)) for i in range(width)]
    left_column = [img.getpixel((0, j)) for j in range(height)]
    right_column = [img.getpixel((width - 1, j)) for j in range(height)]

    # 找到非黑边区域的矩形范围
    left = next((i for i, color in enumerate(left_column) if color != (0, 0, 0)), 0)
    top = next((i for i, color in enumerate(top_row) if color != (0, 0, 0)), 0)
    right = width - next((i for i, color in enumerate(reversed(right_column)) if color != (0, 0, 0)), 0)
    bottom = height - next((i for i, color in enumerate(reversed(bottom_row)) if color != (0, 0, 0)), 0)

    # 防止 left > right 或 top > bottom 的情况
    left, right = min(left, right), max(left, right)
    top, bottom = min(top, bottom), max(top, bottom)

    return left, top, right, bottom

# 替换成你的照片文件夹路径
folder_path = r'C:\Users\willian.zhou\Downloads\test123\123'

# 目标子文件夹路径
destination_folder = os.path.join(folder_path, '123')

# 获取带有黑边的照片列表，裁剪并保存到子文件夹
result = find_photos_with_black_border_and_crop(folder_path, destination_folder)

# 打印结果
for photo_path in result:
    print(photo_path)
