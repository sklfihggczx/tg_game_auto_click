import time
import pyautogui
pyautogui.FAILSAFE = False
time.sleep(5)
pyautogui.click()
print(pyautogui.position()) # 这里获取模拟器位置
print("请最小化程序")
print("Loop completed.")
position_a = (472, 640)  # 根据你的实际情况设置 
position_b = (1011, 639)  # 根据你的实际情况设置

# 循环一百万次
for _ in range(1000000):
    # 移动到a位置并循环一千次
    pyautogui.moveTo(position_a)
    for _ in range(1100):
        pyautogui.click()

    #移动到b位置并循环一千次
    pyautogui.moveTo(position_b)
    for _ in range(1100):
        pyautogui.click()
    #
    #
    time.sleep(1600) #这是等待累积满的时间，单位是秒
