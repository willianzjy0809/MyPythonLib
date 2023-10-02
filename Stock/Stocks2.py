import tkinter as tk
import pandas as pd
from tkinter import ttk
import datetime
from datetime import datetime

# 创建主窗口
root = tk.Tk()
root.title("股票价格跟踪")

# 创建数据保存的数据框，并尝试加载以前保存的数据
try:
    data = pd.read_csv("股票数据.csv", dtype=str)  # 将所有数据都转换为字符串
except FileNotFoundError:
    data = pd.DataFrame(columns=["股票", "日期", "价格"], dtype=str)  # 将索引列设置为False

# 创建标签和文本框，将它们横向排列
label_stock = tk.Label(root, text="股票名称:")
entry_stock = tk.Entry(root)

label_price = tk.Label(root, text="股票价格:")
entry_price = tk.Entry(root)

# 获取当前日期并格式化为字符串
current_date = datetime.now().strftime("%Y-%m-%d")

# 使用StringVar变量来设置日期输入框的默认值
date_var = tk.StringVar()
date_var.set(current_date)

label_date = tk.Label(root, text="日期:")
entry_date = tk.Entry(root, textvariable=date_var)  # 将默认值设置为当前日期

# 使用grid布局将标签和文本框横向排列
label_stock.grid(row=0, column=0)
entry_stock.grid(row=0, column=1)

label_price.grid(row=0, column=2)  # 横向排列，使用了第3列
entry_price.grid(row=0, column=3)  # 横向排列，使用了第4列

label_date.grid(row=0, column=4)  # 横向排列，使用了第5列
entry_date.grid(row=0, column=5)  # 横向排列，使用了第6列

# 保存按钮的回调函数
def save_data():
    stock = entry_stock.get()
    price = entry_price.get()
    date = entry_date.get()
    data.loc[len(data)] = [stock, date, price]
    entry_stock.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    
    # 更新日期变量为当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_var.set(current_date)  # 设置日期输入框的默认值为当前日期
    update_table()

    # 保存数据到 CSV 文件
    data.to_csv("股票数据.csv", index=False, header=True)

# 创建保存按钮，使用grid布局
save_button = tk.Button(root, text="保存", command=save_data)
save_button.grid(row=0, column=6, padx=10)  # 使用了第7列，并添加了一些水平间距

# 创建数据表格
tree = ttk.Treeview(root, columns=("股票", "日期", "价格"), show="headings")
tree.heading("#1", text="股票")
tree.heading("#2", text="日期")
tree.heading("#3", text="价格")
tree.grid(row=1, column=0, columnspan=7)  # 使用了7列，跨足整个表格

# 更新数据表格的函数
def update_table():
    tree.delete(*tree.get_children())
    for index, row in data.iterrows():
        tree.insert("", "end", values=(row["股票"], row["日期"], row["价格"]))

# 显示数据
update_table()

# 删除按钮的回调函数
def delete_data():
    selected_items = tree.selection()
    if selected_items:
        for item in selected_items:
            values = tree.item(item)['values']
            if values:
                # 在数据框中查找匹配的行并删除
                rows_to_delete = data[(data['股票'] == values[0]) & (data['日期'] == values[1]) & (data['价格'] == values[2])]
                if not rows_to_delete.empty:
                    data.drop(rows_to_delete.index, inplace=True)
        
        update_table()
        # 保存更新后的数据到 CSV 文件
        data.to_csv("股票数据.csv", index=False, header=True)

# 创建删除按钮，使用grid布局
delete_button = tk.Button(root, text="删除选中行", command=delete_data)
delete_button.grid(row=2, column=0, columnspan=7, pady=10)

# 启动应用程序
root.mainloop()
