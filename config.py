import ctypes

# Screen configuration
user32 = ctypes.windll.user32
SCREEN_WIDTH, SCREEN_HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Camera resolution
CAM_WIDTH, CAM_HEIGHT = 640, 480

# Gesture control tuning
SMOOTHING_FACTOR = 5
CLICK_DELAY = 0.3