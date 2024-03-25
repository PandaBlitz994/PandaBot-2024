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
    while not 45 < detect_sensor.reflection() < 50:
        chassis.drive(speed=speed,turn_rate=0)
    chassis.brake()
    

        
def run3():
    chassis.settings(straight_speed=700)
    chassis.straight(500)
    right_arm.run_angle(150, 135)
    chassis.straight(-500)

def run2():
    chassis.settings(straight_speed=400)
    chassis.straight(800)
    chassis.settings(straight_speed=700)
    chassis.straight(-1000)
def run1():
    chassis.settings(straight_speed=150)
    chassis.straight(315)
    right_arm.run_angle(speed=120, rotation_angle=130)
    chassis.drive(200, 0)
    wait(2000)
    chassis.brake()
    left_arm.run_time(speed=2000, time=5000)
    chassis.settings(straight_speed=400)
    chassis.turn(-20)
    chassis.straight(30)
    chassis.straight(distance=-650)

def run4():
    chassis.drive(300,0)
    wait(2000)
    chassis.brake()
    chassis.turn(-10)
    chassis.straight(400)
    right_arm.run_angle(200, 180)
    chassis.straight(20)
    chassis.settings(straight_speed=500)
    chassis.straight(-700)

def run5():
    right_arm.run_time(-200, 1000, wait=False)
    until_black_no_follow(right_color, 300)
    chassis.turn(-90)
    chassis.straight(435)
    chassis.turn(35)
    chassis.straight(250)
    chassis.turn(-15)
    chassis.straight(-70)
    chassis.turn(80)
    chassis.straight(-140)
    chassis.turn(-100)
    chassis.straight(-270)
    chassis.turn(-30)
    chassis.straight(-55)
    chassis.turn(-30)
    chassis.turn(30)
    chassis.straight(55)
    chassis.turn(30)
    chassis.straight(300)
    until_bezh(right_color, 200)
    chassis.straight(227)
    right_arm.run_time(300, 1000)
    right_arm.run_time(-300, 1000)
    right_arm.run_time(300, 1000)
    right_arm.run_time(-300, 1000)
    chassis.straight(400)
    chassis.turn(-50)
    left_arm.run_angle(50, 135)
    left_arm.run_angle(20, 45)
    left_arm.run_angle(400, -180)
    chassis.turn(-10)
    chassis.settings(straight_speed=800)
    chassis.straight(700)
def run6():
    chassis.settings(straight_speed=250)
    chassis.straight(750)
    wait(1000)
    chassis.straight(-750)

    
def run7():
    chassis.settings(straight_speed=250)
    
    until_black_no_follow(right_color,200)
    chassis.turn(10)
    chassis.straight(180)
    chassis.straight(-280)
    chassis.turn(30)
    chassis.straight(430)
    chassis.turn(30)
    wait(500)
    chassis.straight(-100)
    chassis.turn(-20)
    chassis.settings(straight_speed=400)
    chassis.straight(-500)


def run9():
        until_bezh(right_color, 200)



def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")




selected = hub_menu(1, 2, 3, 4, 5, 6, 7, 9, 99)


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
elif selected == 6:
    run6()
elif selected == 7:
    run7()
elif selected == 99:
    stats()
elif selected == 9:
    run9()