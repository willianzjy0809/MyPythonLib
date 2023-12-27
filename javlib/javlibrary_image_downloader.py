#这段代码使用Selenium和BeautifulSoup库从javlibrary网站上搜索指定的关键词列表，提取搜索结果页面的电影封面图片，并下载符合条件的图片到本地。

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动Firefox浏览器
browser = webdriver.Firefox()

# 打开网站
browser.get("https://www.javlibrary.com/cn")  # 替换为你的网站URL

# 查找并点击同意按钮
try:
    agree_button = browser.find_element(By.CLASS_NAME, "btnAdultAgree")
    agree_button.click()
except Exception as e:
    print("无法找到同意按钮或点击失败:", str(e))

# 创建一个搜索关键词列表
search_keywords = ["JUQ-296","SSIS-491","SSIS-647","SSIS-708","SSIS-747","SSIS-806","SSIS-843","STARS-238"]  # 替换为你的搜索关键词列表

# 循环搜索和下载图片
for search_query in search_keywords:
    # 查找搜索框并输入搜索关键词
    search_box = browser.find_element(By.NAME, "keyword")  # 替换为实际的搜索框名称或ID
    search_box.clear()  # 清空搜索框
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # 等待URL变化，确保搜索后的URL加载完成
    try:
        WebDriverWait(browser, 10).until(EC.url_changes(browser.current_url))
    except Exception as e:
        print("等待URL变化超时:", str(e))

    # 获取搜索结果页面的URL
    search_result_url = browser.current_url
    print("搜索结果页面的URL:", search_result_url)

    # 发送HTTP请求并解析搜索结果页面的HTML
    response = requests.get(search_result_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所有电影封面的URL
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = img_tag.get('src')

        # 构建完整的图片URL
        if img_url:
            full_img_url = urljoin(search_result_url, img_url)

            # 下载图片
            img_data = requests.get(full_img_url).content

            # 检查图片大小是否小于30KB
            if len(img_data) < 30 * 1024:  # 30 * 1024字节 = 30KB
                continue  # 如果小于30KB，跳过此图片

            img_filename = os.path.basename(full_img_url)
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_data)

# 关闭浏览器
browser.quit()
