import os
import shutil
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 检查是否以管理员权限运行
if not is_admin():
    print("请以管理员权限运行此脚本。")
    exit()

# 关闭Windows外壳程序explorer
os.system('taskkill /f /im explorer.exe')

# 清理系统图标缓存数据库
icon_cache_path = os.path.join(os.getenv('userprofile'), 'AppData', 'Local', 'IconCache.db')

try:
    os.system(f'attrib -h -s -r "{icon_cache_path}"')
    os.remove(icon_cache_path)
except FileNotFoundError:
    print(f'文件不存在: {icon_cache_path}')

explorer_path = os.path.join(os.getenv('userprofile'), 'AppData', 'Local', 'Microsoft', 'Windows', 'Explorer')

# 清理系统图标缓存
thumbcache_files = [
    'thumbcache_32.db',
    'thumbcache_96.db',
    'thumbcache_102.db',
    'thumbcache_256.db',
    'thumbcache_1024.db',
    'thumbcache_idx.db',
    'thumbcache_sr.db'
]

for file_name in thumbcache_files:
    file_path = os.path.join(explorer_path, file_name)
    try:
        os.remove(file_path)
        print(f"文件已删除: {file_path}")
    except FileNotFoundError:
        print(f"文件不存在: {file_path}")
    except PermissionError:
        print(f"没有权限删除文件: {file_path}")

# 清理系统托盘记忆的图标
'''reg_path = r'HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify'
try:
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Software\Microsoft\Windows\CurrentVersion\TrayNotify\IconStreams')
except FileNotFoundError:
    print(f'注册表项不存在: {reg_path}\\IconStreams')

try:
    winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Software\Microsoft\Windows\CurrentVersion\TrayNotify\PastIconsStream')
except FileNotFoundError:
    print(f'注册表项不存在: {reg_path}\\PastIconsStream')
'''
# 重启Windows外壳程序explorer
os.system('start explorer')
