#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
import random


ev3 = EV3Brick()

test_motor = Motor(Port.A)
test_motorb = Motor(Port.B)

ev3.speaker.set_speech_options('en', 'f1', 10, 10)
ev3.speaker.say('<3')
ev3.speaker.beep(500, 2000)

test_motor.run(1000)
test_motorb.run(1000)

while True:
    wait(2000)
    test_motor.run(random.randint(-1050, 1050))
    test_motorb.run(random.randint(-1050, 1050))
    ev3.speaker.beep(frequency=1000, duration=5000)

