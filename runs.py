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


def run9():
    chassis.settings(straight_speed=400)
    chassis.drive(900, 0)

        
        

def run1():
    chassis.settings(straight_speed=180)

    chassis.straight(500)
    right_arm.run_angle(150, 135)
    chassis.straight(-500)


def run2():
    chassis.settings(straight_speed=150)
    chassis.straight(315)
    right_arm.run_angle(speed=120, rotation_angle=130)
    chassis.drive(200, 0)
    wait(2000)
    chassis.brake()
    left_arm.run_time(speed=400, time=4000)
    chassis.settings(straight_speed=400)
    chassis.straight(distance=-450)


def run3():
    left_arm.run_angle(400, 90)
    

def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")




selected = hub_menu(1, 2, 3, 99, 9)


if selected == 1:
    run1()
elif selected == 2:
    run2()
elif selected == 3:
    run3()
elif selected == 99:
    stats()
elif selected == 9:
    run9()
