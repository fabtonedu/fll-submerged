from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__3_trident(motor_config: MotorConfig):

    straight_speed = 1000
    straight_acceleration = 1000
    turn_rate = 500
    turn_acceleration = 120

    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)
    

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
    drive_base.use_gyro(True)


    #kezdodik a program
    drive_base.straight(430)
    drive_base.turn(-39)
    drive_base.straight(400)
    motor_config.b_motor.run_time(speed=-1000, time=1340)
    wait(100)
    drive_base.straight(10)
    wait(400)
    drive_base.straight(-150)
    drive_base.turn(-14)
    motor_config.a_motor.run_time(speed=1000, time=800)
    drive_base.straight(448)
    motor_config.a_motor.run_time(speed=-1000, time=900)
    wait(1500)
    motor_config.a_motor.run_time(speed=1000, time=600)
    drive_base.straight(-100)
    drive_base.turn(-60)
    drive_base.straight(200)
