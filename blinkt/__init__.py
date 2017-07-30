import atexit
from subprocess import PIPE, Popen, check_output


def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels
    If you don't supply a brightness value, the last value set for each pixel be kept.
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
        """
    if brightness is None:
        brightness = -1
    else:
        brightness = int(brightness * 255)
    _send_command("a:%d,%d,%d,%d" % (r, g, b, brightness))


def clear():
    """Clear the pixel buffer"""
    set_all(0, 0, 0)


def set_brightness(brightness: float):
    """Set the brightness of all pixels
    :param brightness: Brightness: 0.0 to 1.0
    """
    if brightness < 0 or brightness > 1:
        raise ValueError("Brightness should be between 0.0 and 1.0")
    _send_command("b:%d" % (int(brightness * 255)))


def set_clear_on_exit(value=True):
    """Set whether Blinkt! should be cleared upon exit
    By default Blinkt! will turn off the pixels on exit, but calling::
        blinkt.set_clear_on_exit(False)
    Will ensure that it does not.
    :param value: True or False (default True)
        """
    _kill_blinkt.kill = value


def set_pixel(x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel
    If you don't supply a brightness value, the last value will be kept.
    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
        """
    if brightness is None:
        brightness = -1
    else:
        brightness = int(brightness * 255)
    _send_command("p:%d,%d,%d,%d,%d" % (x, r, g, b, brightness))


def show():
    """Output the buffer to Blinkt!"""
    _send_command("show")


def _send_command(command: str):
    p.stdin.write(command)
    p.stdin.write("\n")


def _toggel_debug():
    _send_command("debug")


def _run_forever():
    p.wait()


print(check_output('pwd'))
p = Popen("python blinkt/__main__.py",
          shell=True,
          stdin=PIPE,
          universal_newlines=True,
          bufsize=1
          )


def _kill_blinkt():
    if _kill_blinkt.kill:
        p.kill()


set_clear_on_exit(True)
atexit.register(_kill_blinkt)
