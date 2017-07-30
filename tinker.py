import time
from blinkt import set_pixel, set_brightness, show, clear, _toggel_debug, _run_forever

# _toggel_debug()
# _run_forever()

set_brightness(0.3)
while True:
    for i in range(8):
        clear()
        set_pixel(i, 255, 0, 0)
        show()
        time.sleep(0.05)
