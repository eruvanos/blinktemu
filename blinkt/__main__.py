import sys
from queue import Queue
from sys import stdin
from threading import Thread

import arcade
from copy import deepcopy

NUMBER_LEDS = 8
RECT_SIZE = 50
RECT_BORDER = 1
OFF_COLOR = (0, 0, 0, 0)


def log(*args):
    if log.debugging_enabled:
        print(*args)


log.debugging_enabled = False


class Pixel:
    def __init__(self, color):
        self.color = color


class StdInReader(Thread):
    def __init__(self, queue):
        super().__init__(daemon=True)
        self.queue: Queue = queue

    def run(self):
        while True:
            self.queue.put(stdin.readline())


class BlinktVisual(arcade.Window):
    def __init__(self):
        super().__init__(RECT_SIZE * NUMBER_LEDS, RECT_SIZE, title="Blinkt")

        self.leds = [Pixel(OFF_COLOR) for _ in range(NUMBER_LEDS)]
        self.public_leds = deepcopy(self.leds)

        self.queue = Queue()
        self.stdin_reader = StdInReader(self.queue)
        self.stdin_reader.start()

    def on_draw(self):
        arcade.start_render()
        for i in range(8):
            x = (RECT_SIZE / 2) + i * RECT_SIZE
            y = (RECT_SIZE / 2)

            led_color = self.public_leds[i].color
            arcade.draw_rectangle_filled(x, y, RECT_SIZE, RECT_SIZE, led_color)
            arcade.draw_rectangle_outline(x, y,
                                          RECT_SIZE, RECT_SIZE,
                                          arcade.color.RED,
                                          RECT_BORDER)

    def update(self, dt):
        log("empty?: %s" % self.queue.empty())
        if not self.queue.empty():
            try:
                readlines = self.queue.get()
                self.process_command(readlines.strip())
            except:
                log("Error %s" % str(sys.exc_info()))
        else:
            log("No input")

    def process_command(self, command: str):
        log("Input: %s\n" % command)
        if command == "show":
            self.public_leds = deepcopy(self.leds)
            return
        elif command.startswith("p:"):
            x, *color = [int(v) for v in command[2:].split(",")]

            # Keep brightness if not given
            if color[3] == -1:
                color[3] = self.leds[x].color[3]

            self.leds[x].color = color
        elif command.startswith("b:"):
            brightness = int(command[2:])
            for l in self.leds:
                l.color = l.color[:-1] + (brightness,)
        elif command == "debug":
            log.debugging_enabled = not log.debugging_enabled
        else:
            log("Unknown command: %s" % command)


def main():
    BlinktVisual()
    arcade.run()


main()
