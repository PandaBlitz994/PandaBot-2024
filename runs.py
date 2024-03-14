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
right_color= ColorSensor(Port.A)
left_color= ColorSensor(Port.E)
chassis.use_gyro(True)


def follow_line_with_time(time, speed, kp, side, sensor):
    target = 50
    left_motor.reset_angle()
    if side == "left":
        kp *= -1
    while (left_motor.angle() < distance):
        error = target - sensor.reflection()
        left_motor.dc(int(speed + error * kp))
        right_motor.dc(int(speed - error * kp))
    left_motor.stop()
    right_motor.stop()

def follow_line(distance, speed, kp, side, sensor):
    target = 50
    left_motor.reset_angle()
    if side == "left":
        kp *= -1
    while (left_motor.angle() < distance):
        error = target - sensor.reflection()
        left_motor.dc(int(speed + error * kp))
        right_motor.dc(int(speed - error * kp))
    left_motor.stop()
    right_motor.stop()

def until_black(detect_sensor, speed, kp, side, follow_sensor):
    target = 50
    if side == "left":
        kp *= -1
    while detect_sensor.reflection() > 11:
        error = target - follow_sensor.reflection()
        left_motor.dc(int(speed + error * kp))
        right_motor.dc(int(speed - error * kp))
    left_motor.stop()
    right_motor.stop()

def until_black_no_follow(detect_sensor, speed):
    while detect_sensor.reflection() > 10:
        chassis.drive(speed=speed,turn_rate=0)
    chassis.brake()

def until_bezh(detect_sensor, speed):
    while 45 < detect_sensor.reflection() < 50:
        chassis.drive(speed=speed,turn_rate=0)
    chassis.brake()
    
def run9():
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
    right_arm.run_time(-200, 1000, wait=False)
    until_black_no_follow(right_color, 300)
    chassis.turn(-90)
    chassis.straight(450)
    chassis.turn(35)
    chassis.straight(250)
    chassis.turn(-15)
    chassis.straight(-70)
    chassis.turn(80)
    chassis.straight(-140)
    chassis.turn(-100)
    until_bezh(right_color, 200)
    chassis.straight(280)
    right_arm.run_time(300, 1000)
    right_arm.run_time(300,1000)
    right_arm.run_time(-300, 1000)

def run4():
    chassis.settings(straight_speed=300)
    chassis.straight(500)
    until_black_no_follow(right_color,300)
    chassis.straight(100)
    chassis.turn(-60)
    right_arm.run_time(speed=300,time=1500)
    chassis.straight(-80)
    chassis.turn(80)
    chassis.settings(straight_speed=500)
    chassis.straight(-650)

    #chassis.straight(750)
    #chassis.settings(straight_speed=400)f
    #chassis.straight(-750)
    
def run5():
    right_arm.run_time(speed=-700,time=4000)

# def run9():
#     chassis.settings(straight_speed=500)
#     chassis.straight(10000)



def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")




selected = hub_menu(1, 2, 3, 4, 5, 33, 9, 99)


if selected == 1:
    run1()
elif selected == 2:
    run2()
elif selected == 3:
    run3()
elif selected == 4:
    run4()
elif selected == 5:
    run5()
elif selected == 33:
    run33()
elif selected == 99:
    stats()
elif selected == 9:
    run9()