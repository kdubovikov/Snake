__author__ = 'kernel_mode'
from threading import Thread
from time import sleep
from screen import utils

class GameLoop(Thread):
    objects = []
    interval = 0.5

    def __init__(self, interval):
        super().__init__()
        self.interval = interval
        self._terminate = False

    def stop(self):
        self._terminate = True

    def run(self):
        while not self._terminate:
            for obj in self.objects:
                utils.cls()
                obj.render()
                obj.update()
            sleep(self.interval)
