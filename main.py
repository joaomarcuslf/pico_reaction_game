from machine import Pin
from time import sleep, ticks_ms, ticks_diff
from random import uniform

main_led = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT)

main_led.on()

pressed = False

def button_handler(pin):
    global pressed

    if not pressed:
        pressed = True
        reaction_time = ticks_diff(ticks_ms(), start_time)
        print("Reaction time: {} ms".format(reaction_time))

led.value(1)
sleep(uniform(5, 10))
led.value(0)

start_time = ticks_ms()

button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
