import ctypes

def move_cursor(x, y):
    ctypes.windll.user32.SetCursorPos(int(x), int(y))