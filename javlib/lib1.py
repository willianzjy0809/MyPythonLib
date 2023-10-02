import requests
from bs4 import BeautifulSoup
import openpyxl

# 创建一个Excel工作簿
wb = openpyxl.Workbook()
ws = wb.active

# 添加Excel表头
ws.append(['ID', 'Maker', 'Cast'])

# 定义爬取网页的URL
url = 'https://www.javlibrary.com/en/?v=javmefrg34'

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用Beautiful Soup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取<head><title>元素内容作为ID
    head = soup.find('head')
    title_element = head.find('title')
    id = title_element.text.strip()

    # 将ID添加到Excel中
    ws.append([id, '', ''])  # 在此示例中，ID写入第一列，Maker和Cast列留空

    # 找到包含信息的表格
    table = soup.find('table')

    # 遍历表格的行
    for row in table.find_all('tr'):
        # 找到每行中的列
        cols = row.find_all('td')
        if len(cols) == 3:  # 假设每行有3列：ID、Maker和Cast
            maker = cols[0].text.strip()
            cast = cols[1].text.strip()

            # 将信息添加到Excel中
            ws.append(['', maker, cast])  # 在此示例中，ID列留空，Maker和Cast写入后两列

    # 保存Excel文件
    wb.save('output.xlsx')
else:
    print('无法访问网页')
