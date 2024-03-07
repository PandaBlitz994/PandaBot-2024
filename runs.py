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
    while detect_sensor.reflection() > 20:
        chassis.drive(speed=speed,turn_rate=0)
    chassis.stop
    
def run9():
    chassis.settings(straight_speed=400)
    chassis.drive(900, 0)

        
        

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
    chassis.settings(straight_speed=350)
    chassis.straight(455)
    chassis.turn(-65)
    #chassis.turn(10)
    chassis.straight(800) 
    # chassis.straight(130)
    
    chassis.straight(-225)
    chassis.turn(40)
    chassis.straight(40)
    chassis.turn(15)
    chassis.straight(-135)
    chassis.turn(40)
    chassis.straight(110)
    chassis.turn(-30)
    # chassis.turn(-30)
    # chassis.straight(50)
    # chassis.straight(-20)
    # chassis.turn(4)
    # chassis.straight(-100)
    # chassis.turn(40)
    # chassis.straight(-200)
    # wait(100)
    # chassis.turn(10)
    # chassis.straight(-30)
    
    #until_black_no_follow(detect_sensor=right_color,speed=120)
    #follow_line(distance=905, speed=40, kp=0.7, side="right", sensor=right_color)
    #until_black(detect_sensor=right_color, speed=40, kp=0.25, side="right", follow_sensor=left_color)
    #left_motor.run_angle(350,265)
    #chassis.straight(240)
    #right_motor.run_angle(350,420)
    #follow_line(distance=205, speed=40, kp=0.8, side="right", sensor=left_color)
    #chassis.straight(485)
    #left_motor.run_angle(350,110)
    #left_motor.run_angle(350,425)
    #chassis.straight(150)
    #chassis.straight(-50)
    #right_motor.run_angle(200,60)
    #chassis.straight(-300)
    #chassis.straight(-110)
    
    #left_motor.run_angle(350,25)
    #chassis.straight(-210)
    

    # chassis.straight(400)
    # chassis.turn(angle=-65)
    # chassis.straight(980)
    # chassis.turn(angle=20)
    # #   chassis.straight(-150)
    # chassis.straight(-310)
    # chassis.turn(angle=100)
    # chassis.straight(-95)
    # chassis.turn(angle=40)
    # chassis.straight(100)

def run33():
    chassis.settings(straight_speed=250)
    chassis.straight(69)
    chassis.turn(45)
    chassis.straight(455)
    chassis.turn(-65)
    chassis.straight(710) 
    chassis.straight(-115)
    chassis.turn(60)
    chassis.turn(-30)
    chassis.straight(-50)
    chassis.turn(-25)
    chassis.straight(-40)
    chassis.turn(-40)
    chassis.straight(-50)
    chassis.turn(-20)
    chassis.straight(150)
    chassis.turn(-30)
    chassis.straight(30)
    chassis.turn(60)
    chassis.straight(325)
    right_arm.run_angle(speed=200, rotation_angle=200)
    right_arm.run_angle(speed=200, rotation_angle=-200)
    #right_arm.run_angle(500,200)
    chassis.straight(430)
    chassis.turn(-60)
    left_arm.run_angle(speed=200, rotation_angle=200)
    left_arm.run_angle(speed=200, rotation_angle=-200)
    #chassis.straight(1000)



def run4():
    chassis.settings(straight_speed=180)
    chassis.straight(700)
    chassis.straight(-700)
    

def run9():
    chassis.settings(straight_speed=500)
    chassis.straight(10000)

def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")




selected = hub_menu(1, 2, 3, 4,33, 9, 99)


if selected == 1:
    run1()
elif selected == 2:
    run2()
elif selected == 3:
    run3()
elif selected == 4:
    run4()
elif selected == 33:
    run33()
elif selected == 99:
    stats()
elif selected == 9:
    run9()