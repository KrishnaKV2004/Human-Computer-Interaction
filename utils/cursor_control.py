import ctypes

def left_click():
    ctypes.windll.user32.mouse_event(0x02, 0, 0, 0, 0)  # Left down
    ctypes.windll.user32.mouse_event(0x04, 0, 0, 0, 0)  # Left up

def right_click():
    ctypes.windll.user32.mouse_event(0x08, 0, 0, 0, 0)  # Right down
    ctypes.windll.user32.mouse_event(0x10, 0, 0, 0, 0)  # Right up

def drag_start():
    ctypes.windll.user32.mouse_event(0x02, 0, 0, 0, 0)  # Left down

def drag_end():
    ctypes.windll.user32.mouse_event(0x04, 0, 0, 0, 0)  # Left up