import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

btn1_pin = board.GP1
btn2_pin = board.GP2
btn3_pin = board.GP3
btn4_pin = board.GP4
btn5_pin = board.GP5
btn6_pin = board.GP6
btn7_pin = board.GP7
btn8_pin = board.GP8
btn9_pin = board.GP9
led1_pin = board.GP12
led2_pin = board.GP13
led3_pin = board.GP14


btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN
keyboard = Keyboard(usb_hid.devices)
led1 = digitalio.DigitalInOut(led1_pin)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(led2_pin)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(led3_pin)
led3.direction = digitalio.Direction.OUTPUT
led1.value = True
led2.value = True
led3.value = True

while True:
    led1.value = True
    led2.value = True
    led3.value = True
    if btn1.value:
        keyboard.send(Keycode.ONE)
        time.sleep(0.15)
    if btn2.value:
        keyboard.send(Keycode.FOUR)
        time.sleep(0.15)
    if btn3.value:
        keyboard.send(Keycode.SEVEN)
        time.sleep(0.15)
    if btn4.value:
        keyboard.send(Keycode.TWO)
        time.sleep(0.15)
    if btn5.value:
        keyboard.send(Keycode.FIVE)
        time.sleep(0.15)
    if btn6.value:
        keyboard.send(Keycode.EIGHT)
        time.sleep(0.15)
    if btn7.value:
        keyboard.send(Keycode.THREE)
        time.sleep(0.15)
    if btn8.value:
        keyboard.send(Keycode.SIX)
        time.sleep(0.15)
    if btn9.value:
        keyboard.send(Keycode.NINE)
        time.sleep(0.15)
    time.sleep(0.1)
