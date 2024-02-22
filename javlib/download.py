import requests
from bs4 import BeautifulSoup
import os
import openpyxl

def download_file(url, destination_folder):
    response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]
    file_path = os.path.join(destination_folder, file_name)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)
    print(f"{file_name} downloaded successfully.")

def batch_download_links_from_excel(excel_file, sheet_name, start_row, end_row, column, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook[sheet_name]

    links = [sheet[f"{column}{row}"].value for row in range(start_row, end_row + 1)]

    for link in links:
        download_file(link, destination_folder)

# 示例 Excel 文件名和工作表名
excel_file = "output.xlsx"
sheet_name = "Sheet1"  # 你的工作表名
start_row = 14          # 起始行
end_row = 20           # 结束行
column = "C"           # 列名，即 C 列

# 设置下载目录
download_folder = "downloads"

# 执行批量下载
batch_download_links_from_excel(excel_file, sheet_name, start_row, end_row, column, download_folder)
