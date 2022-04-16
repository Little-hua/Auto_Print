import imp
import time
from unicodedata import name
from unittest import result
import cv2
import pyautogui
import os

# 用来判定画面的点击坐标
# 输入图片路径
# 返回一个元组，检测区域中心的坐标
def get_xy(moban):
    # 保存屏幕截图
    pyautogui.screenshot().save(r'C:\Users\Administrator\Documents\zhutu.png')
    # 载入截图
    img = cv2.imread(r'C:\Users\Administrator\Documents\zhutu.png')
    # 图像模板
    img_terminal = cv2.imread(moban)
    # 读取模板的宽度和高度
    height,width,channe = img_terminal.shape   #i=(height,width)
    # 进行模板匹配
    result = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED)
    #解析出匹配区域的左上角坐标
    upper_left = cv2.minMaxLoc(result)[2]
    # 计算匹配区域右下角的坐标
    lower_right = (upper_left[0]+width,upper_left[1]+height)
    # 计算中心区域坐标并返回
    avg = (int((upper_left[0]+lower_right[0])/2),int((upper_left[1]+lower_right[1])/2))
    return avg

# 接受一个元组参数，鼠标单击
def auto_click(zuobiao):
    pyautogui.click(zuobiao[0],zuobiao[1])#(zuobiao[0],zuobiao[1])
    time.sleep(1)
# 接受一个元组参数，鼠标双击
def auto_doubleclick(zuobiao):
    pyautogui.doubleClick(zuobiao[0],zuobiao[1])
    time.sleep(1)

# 单击选中图片
def routine(img_model_path,name):
    avg = get_xy(img_model_path)
    print(f'正在点击{name}')
    auto_click(avg)
# 双击选中图片
def routine_double(img_model_path,name):
    avg = get_xy(img_model_path)
    print(f'正在点击{name}')
    auto_doubleclick(avg)



routine_double(r"C:\Users\Administrator\Desktop\mycode\555\tupian\dayinwenjiajia.png",'选中打印文件夹')
time.sleep(0.3)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\chakan.png",'查看')
time.sleep(0.3)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\tubiao.png",'选中中图标')
time.sleep(0.3)
routine_double(r"C:\Users\Administrator\Desktop\mycode\555\tupian\world.png",'双击打开world')
time.sleep(3)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\dayin.png",'点击打印')
time.sleep(1)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\suofang.png",'选择缩放')
time.sleep(0.5)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\A4.png",'选中A4')
time.sleep(0.5)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\queding.png",'点击确定')
time.sleep(5)
routine(r"C:\Users\Administrator\Desktop\mycode\555\tupian\xx.png",'关闭文件')