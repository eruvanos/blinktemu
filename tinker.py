import colorsys
import datetime
import time
from blinkt import set_pixel, set_brightness, show, clear, _toggel_debug, _run_forever, set_all

# _toggel_debug()
# _run_forever()

# BENCHMARK
# start = datetime.datetime.utcnow()
# for i in range(10000):
#     set_all(255, 0, 0)
#     show()
#
# print("Time: %s" % (datetime.datetime.utcnow() - start))

# WALKING PIXEL
set_brightness(0.3)
while True:
    for i in range(8):
        clear()
        set_pixel(i, 255, 0, 0)
        show()
        time.sleep(0.05)

# RAINBOW
# set_brightness(0.3)
# spacing = 360.0 / 16.0
# hue = 0
# while True:
#     hue = int(time.time() * 100) % 360
#     for x in range(8):
#         offset = x * spacing
#         h = ((hue + offset) % 360) / 360.0
#         r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
#         set_pixel(x, r, g, b)
#     show()
#     time.sleep(0.001)