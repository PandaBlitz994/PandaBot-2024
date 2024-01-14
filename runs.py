from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub
left_motor = Motor(Port.F,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
left_arm =Motor(Port.D)
right_arm =Motor(Port.C)
chassis = DriveBase(left_motor,right_motor,56,114)
chassis.use_gyro(True)


def run1():
    chassis.settings(straight_speed=140)
    for i in range(3):
        chassis.straight(90)
        chassis.straight(-60)
        wait(300)
        
    #chassis.turn(90,Stop.HOLD,wait=True)

def run2():
    chassis.straight(100)
    right_arm.run_angle(350,-600)
        

def run3():
     left_arm.run_angle(400,90)





selected = hub_menu("1", "2", "3")


if selected == "1":
    run1()
elif selected == "2":
    run2()
elif selected == "3":
    run3()