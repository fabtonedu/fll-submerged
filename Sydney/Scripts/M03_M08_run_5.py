from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__5_coralls(motor_config: MotorConfig):
    


    straight_speed = 1000
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration =500


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot
    drive_base.curve(radius=3800, angle=10)
    wait(100)
    #felállitjuk a rákketreceket
    drive_base.settings(1000, 1000, 500, 500)
    wait(100)
    #átforditjuk őket 40 pontosra
    drive_base.turn(-5)
    drive_base.straight(600)
    drive_base.settings(1000, 500, 250, 250)
    #miután előrementünk, kiengedjük a korallokat, úgy hogy álljanak a térképen
    motor_config.a_motor.run_time(speed=-400, time=500)
    wait(50)
    drive_base.straight(-100)
    #visszamegyünk a bázisra
    drive_base.turn(-26)
    drive_base.curve(radius=-1600, angle=-17)
    drive_base.straight(-300)
    drive_base.curve(radius=-200, angle=-70)
    drive_base.straight(-200)