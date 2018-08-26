'''
打印按键的状态
'''

from machine import Pin
import utime

# 引脚
button = Pin(5, Pin.IN)

# 定义按键按下的值 （取决于按键模块的设计， 有可能相反）
BTN_DOWN = 0 # 按键按下对应的取值 
BTN_UP = 1 # 按键抬起对应的状态

while True:
    # 获取按钮状态
    btn_status = button.value()

    if btn_status == BTN_DOWN:
        print("按键状态：按下")
    else:
        print("按键状态：抬起")
    # 延时500ms
    utime.sleep_ms(500)
