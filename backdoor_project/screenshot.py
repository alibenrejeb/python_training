import time
from PIL import ImageGrab

screenshot = ImageGrab.grab()
# screenshot.show()
screenshot.save(f'screenshot_{int(time.time())}.png', 'PNG')
