from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()
left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
left_arm = Motor(Port.D)
right_arm = Motor(Port.C)
chassis = DriveBase(left_motor, right_motor, 56, 114)
chassis.use_gyro(True)


def run1():
    chassis.settings(straight_speed=180)

    chassis.straight(500)
    right_arm.run_angle(150, 150)
    chassis.straight(-500)


def run2():
    chassis.straight(100)
    right_arm.run_angle(350, -600)


def run3():
    left_arm.run_angle(400, 90)


def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")


selected = hub_menu(1, 2, 3, 99)


if selected == 1:
    run1()
elif selected == 2:
    run2()
elif selected == 3:
    run3()
elif selected == 99:
    stats()
