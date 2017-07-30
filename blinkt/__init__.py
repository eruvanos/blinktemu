from subprocess import PIPE, Popen, check_output


def set_all(r, g, b, brightness=None):
    for i in range(8):
        set_pixel(i, r, g, b, brightness=brightness)


def clear():
    set_all(0, 0, 0)


def set_brightness(brightness: float):
    _send_command("b:%d" % (int(brightness * 255)))


def set_clear_on_exit(value=True):
    pass


def set_pixel(x, r, g, b, brightness=None):
    if brightness is None:
        brightness = -1
    else:
        brightness = int(brightness * 255)
    _send_command("p:%d,%d,%d,%d,%d" % (x, r, g, b, brightness))


def show():
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
