import msvcrt
from threading import Thread

class InputEvent:
    listeners = []

    def fire(self, key):
        for l in self.listeners:
            l(key)


class InputEventLoop(Thread):
    input_event = InputEvent()

    def __init__(self):
        super().__init__()
        self._terminate = False

    def stop(self):
        self._terminate = True

    def add_input_listener(self, listener):
        self.input_event.listeners.append(listener)

    def run(self):
        while not self._terminate:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                self.input_event.fire(key)
    
