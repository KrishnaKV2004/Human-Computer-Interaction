import ctypes

# Screen configuration
user32 = ctypes.windll.user32
SCREEN_WIDTH, SCREEN_HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Camera resolution
CAM_WIDTH, CAM_HEIGHT = 640, 480

# Cursor smoothing and click delay
SMOOTHING_FACTOR = 5
CLICK_DELAY = 0.3

# Gesture control tuning
FRAME_THRESHOLD = 5                 # Frames for stable gesture (right click)
CLICK_DIST_THRESHOLD = 25           # Distance threshold for pinch gestures
CLICK_HYSTERESIS = 3                # Buffer to reduce flicker
DRAG_HOLD_DELAY = 0.4               # Seconds to hold pinch before triggering drag