import subprocess

# 将 Windows 用户账户控制（UAC）的提示级别设置为最低
def set_uac_prompt_level():
    try:
        subprocess.run(["reg", "add", "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "/v", "ConsentPromptBehaviorAdmin", "/t", "REG_DWORD", "/d", "0", "/f"], check=True)
        print("Windows 用户账户控制（UAC）的提示级别已设置为最低。")
    except subprocess.CalledProcessError as e:
        print("无法设置 Windows 用户账户控制（UAC）的提示级别：", e)

# 使用函数来设置 UAC 提示级别
set_uac_prompt_level()
