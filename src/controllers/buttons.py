from gpiozero import Button
from dataclasses import dataclass
from signal import pause
from threading import Thread
from queue import Queue
from time import sleep

@dataclass
class ButtonInfo:
    board_pin: int
    gpio: int
    label: str
    button: Button

class BUTTON_LABEL:
    BTN_0 = "0"
    BTN_1 = "1"
    BTN_2 = "2"
    BTN_3 = "3"
    BTN_4 = "4"
    BTN_5 = "5"
    BTN_6 = "6"
    BTN_7 = "7"
    BTN_8 = "8"
    BTN_9 = "9"
    BTN_BRANCO = "BRANCO"
    BTN_CORRIGE = "CORRIGE"
    BTN_CONFIRMA = "CONFIRMA"

button_array = []
button_array.append(ButtonInfo(3,   2,  BUTTON_LABEL.BTN_0, None))
button_array.append(ButtonInfo(5,   0,  BUTTON_LABEL.BTN_1, None))
button_array.append(ButtonInfo(7,   11,  BUTTON_LABEL.BTN_2, None))
button_array.append(ButtonInfo(11,  9, BUTTON_LABEL.BTN_3, None))
button_array.append(ButtonInfo(13,  10, BUTTON_LABEL.BTN_4, None))
button_array.append(ButtonInfo(15,  22, BUTTON_LABEL.BTN_5, None))
button_array.append(ButtonInfo(19,  27, BUTTON_LABEL.BTN_6, None))
button_array.append(ButtonInfo(21,  17,  BUTTON_LABEL.BTN_7, None))
button_array.append(ButtonInfo(23,  4, BUTTON_LABEL.BTN_8, None))
button_array.append(ButtonInfo(27,  3,  BUTTON_LABEL.BTN_9, None))
button_array.append(ButtonInfo(29,  13,  BUTTON_LABEL.BTN_BRANCO, None))
button_array.append(ButtonInfo(31,  6,  BUTTON_LABEL.BTN_CORRIGE, None))
button_array.append(ButtonInfo(33,  5, BUTTON_LABEL.BTN_CONFIRMA, None))

def check_button_state(button_queue):
    button_state = {}
    for btn in button_array:
        button_state[btn.label] = False

    while True:
        for btn in button_array:
            btn_state = btn.button.is_pressed

            if button_state[btn.label] != btn_state:
                if btn_state:
                    button_queue.put(btn.label)

                button_state[btn.label] = btn_state

        sleep(0.01)


class Buttons:
    def __init__(self):
        for btn in button_array:
            btn.button = Button(btn.gpio)

        self.btn_pressed_queue = Queue()
        self.thread_check_buttons = Thread(target=check_button_state, args=(self.btn_pressed_queue,))
        self.thread_check_buttons.start()

    def check_buttons(self):
        if self.btn_pressed_queue.qsize() == 0:
            return None

        return self.btn_pressed_queue.get(block=False, timeout=None)

    def flush_queue(self):
        while self.btn_pressed_queue.qsize() > 0:
            self.btn_pressed_queue.get(block=False, timeout=None)