__author__ = 'kernel_mode'
from core.events import InputEventLoop
from core.entities import Snake
from core.game_loop import GameLoop
import core.input_constants
import colorama

colorama.init()

game_loop = GameLoop(0.5)
event_loop = InputEventLoop()

def main_input_listener(key):
    if key == core.input_constants.ESC:
        event_loop.stop()
        event_loop.join()

        game_loop.stop()
        game_loop.join()
        quit()

if __name__ == '__main__':
    snake = Snake()

    game_loop.objects.append(snake)
    event_loop.add_input_listener(snake.on_input)
    event_loop.add_input_listener(main_input_listener)

    event_loop.start()
    game_loop.start()