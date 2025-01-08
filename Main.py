import time

import pynput.mouse
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController

# ----------
# python 3.1.2
# FreePiano_auto
# 版权所有 (C) 2025年 狼元星

# 这个文件是 FreePiano_auto 的一部分。

# FreePiano_auto 是自由软件：您可以根据自由软件基金会发布的GNU通用公共许可证的条款重新分发和/或修改它，无论是许可证的第三版，还是（根据您的选择）任何后续版本。

# 这个程序是希望它能够有用，但不附带任何形式的保证；甚至不包括适销性或特定用途适用性的暗示保证。有关更多详细信息，请参阅GNU通用公共许可证。

# 您应该已经收到一份GNU通用公共许可证的副本，与这个程序一起。如果没有，请访问 http://www.gnu.org/licenses/。
# ------------

# 创建键盘和鼠标对象
mouse = MouseController()
keyboard = KeyboardController()

# 把FreePiano移动到屏幕左上角
# 设置鼠标位置到 (800, 10)并点击,以确保在 FreePiano 输入
mouse.position = (500, 10)
mouse.click(pynput.mouse.Button.left)


# 使用函数模拟点击操作
def dotted_whole(key):
    # 附点全音符
    keyboard.press(key)
    time.sleep(3.75)
    keyboard.release(key)


def whole(key):
    # 全音符
    keyboard.press(key)
    time.sleep(2.5)
    keyboard.release(key)


def dotted_half(key):
    # 附点二分音符
    keyboard.press(key)
    time.sleep(1.875)
    keyboard.release(key)


def half(key):
    # 二分音符
    keyboard.press(key)
    time.sleep(1.25)
    keyboard.release(key)


def dotted_quarter(key):
    # 附点四分音符
    keyboard.press(key)
    time.sleep(0.9375)
    keyboard.release(key)


def quarter(key):
    # 四分
    keyboard.press(key)
    time.sleep(0.625)
    keyboard.release(key)


def dotted_eighth(key):
    # 附点八分音符
    keyboard.press(key)
    time.sleep(0.46875)
    keyboard.release(key)


def eighth(key):
    # 八分
    keyboard.press(key)
    time.sleep(0.3125)
    keyboard.release(key)


def dotted_sixteenth(key):
    # 附点十六分音符
    keyboard.press(key)
    time.sleep(0.234375)
    keyboard.release(key)


def sixteenth(key):
    # 十六分
    keyboard.press(key)
    time.sleep(0.15625)
    keyboard.release(key)


def staccato_sixteenth(key):
    # 十六分加上减时线
    keyboard.press(key)
    time.sleep(0.078125)
    keyboard.release(key)


def sustain():
    # 延音
    keyboard.press(Key.esc)
    time.sleep(0.1)  # 稍微等待一下，确保Esc键被注册
    keyboard.release(Key.esc)


# 以下为演奏区(欢乐颂一小部分,力度建议32,减去一个八度,为mdaPiano)
quarter('3')
quarter('3')
quarter('4')
quarter('5')
# ------------
quarter('5')
quarter('4')
quarter('3')
quarter('2')
# ------------
quarter('1')
quarter('1')
quarter('2')
quarter('3')
# ------------
dotted_quarter('3')
sixteenth('2')
half('2')
time.sleep(0.625)  # 休止
# ------------
quarter('3')
quarter('3')
quarter('4')
quarter('5')
# -------------------
quarter('5')
quarter('4')
quarter('3')
quarter('2')
# ------------
quarter('1')
quarter('1')
quarter('2')
quarter('3')
# ------------
dotted_quarter('2')
eighth('1')
quarter('1')
time.sleep(0.625)  # 休止
# ------------
quarter('2')
quarter('2')
quarter('3')
quarter('1')
# ------------
quarter('2')
eighth('3')
eighth('4')
quarter('3')
quarter('1')
time.sleep(0.625)  # 休止
# -------------------
