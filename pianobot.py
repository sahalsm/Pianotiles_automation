import pyautogui
import time
import keyboard
import win32api , win32con

# X:  727 Y:  687 RGB: (255, 255, 255)
# X:  880 Y:  624 RGB: (255, 255, 255)
# X: 1057 Y:  714 RGB: (255, 255, 255)
# X: 1199 Y:  683 RGB: (255, 255, 255)


def click(x,y):

    # pyautogui.moveTo(x,y,0.01)
    # pyautogui.click(x,y)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pix1 = pyautogui.pixel(700,569)[0]
    pix2 = pyautogui.pixel(795,569)[0]
    pix3 = pyautogui.pixel(874,569)[0]
    pix4 = pyautogui.pixel(960,569)[0]
    # print(pix1)
    # print(pix2)
    # print(pix3)
    # print(pix4)
    # if pyautogui.pixel(700,569)[0] == 0:q
    #     click(700,569)
    # if pyautogui.pixel(795,569)[0] == 0:
    #     click(795,569)
    # if pyautogui.pixel(874,569)[0] == 0:
    #     click(874,569)
    # if pyautogui.pixel(960,569)[0] == 0:
    #     click(960,569)

    if pix1 == 0:
        click(700,569)
    if pix2 == 0:
        click(795,569)
    if pix3 == 0:
        click(874,569)
    if pix4 == 0:
        click(960,569)
