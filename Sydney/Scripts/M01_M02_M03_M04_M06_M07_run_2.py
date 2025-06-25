from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__2_scuba(motor_config: MotorConfig):
    


    straight_speed = 700
    straight_acceleration = 600
    turn_rate = 250
    turn_acceleration = 120

    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot
    #kihajtunk a bázisról
    drive_base.straight(distance=-60)
    drive_base.turn(angle=42)
    drive_base.straight(distance=-380)
    drive_base.turn(angle=47)
    #nekimegyünk a hajóroncsnak, felállitjuk, és kihalásszuk a ládát alóla
    drive_base.settings(550, 450, 500, 120)
    drive_base.straight(distance=-300)
    wait(50)
    drive_base.straight(distance=120)
    drive_base.settings(700, 600, 500, 120)
    drive_base.turn(angle=78)
    drive_base.straight(distance=122)
    drive_base.turn(angle=-72)
    #leengedjük mindkét kart a búvárhoz és korallfához
    motor_config.a_motor.run_time(speed=-999, time=830)
    drive_base.settings(200, 150, 500, 120)
    motor_config.b_motor.run_time(speed=-300, time=680)
    #benyomjuk a korallfa előtt található billentyűt
    drive_base.straight(distance=105)
    #felakasztjuk a korallfát
    motor_config.a_motor.run_time(200, 2125)
    motor_config.a_motor.run_time(-200, 800)
    #kiemeljük a búvárt
    motor_config.b_motor.run_time(speed=800, time=350)
    wait(100)
    drive_base.straight(-60)
    #átmegyünk a korallokhoz
    drive_base.curve(radius=-90, angle=-81)
    drive_base.straight(92)
    #felakasztjuk a búvárt
    motor_config.b_motor.run_time(-400, 340)
    wait(100)
    drive_base.straight(-70)
    drive_base.turn(-0.7)
    #leütjük ay itt található billentyűt, hogy kiemelkedjen a korallkert
    drive_base.settings(300, 300, 150, 150)
    motor_config.b_motor.run_time(1000, 700)
    drive_base.straight(68)
    wait(100)
    #átmegyünk a cápához, és leengedjük azt is
    motor_config.b_motor.run_time(-1000, 900)
    wait(200)
    motor_config.b_motor.run_time(1000, 100)
    drive_base.turn(-5)
    motor_config.b_motor.run_time(1000, 700)
    #visszamegyünk a bázisra
    drive_base.straight(-30)
    drive_base.turn(-50)
    drive_base.straight(77)
    motor_config.b_motor.run_time(speed=-1000, time=1000)
    motor_config.b_motor.run_time(speed=1000, time=1000)
    drive_base.settings(900, 900, 250, 250)
    drive_base.curve(radius=-100, angle=-85.0)
    drive_base.straight(-600)