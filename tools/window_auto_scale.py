from win32.lib import win32con
from win32 import win32gui,win32print

# 获取屏幕物理分辨率
def get_real_screen_resolution()->dict:
    hDC = win32gui.GetDC (0)
    width = win32print.GetDeviceCaps (hDC,win32con.DESKTOPHORZRES)
    height = win32print.GetDeviceCaps (hDC,win32con.DESKTOPVERTRES)
    return {"width":width,"height":height}


def calculate_screen_scaling_ratio()->float:
    screen_size = get_real_screen_resolution()
    ratio = screen_size["width"] / 1920
    return ratio * 1.2