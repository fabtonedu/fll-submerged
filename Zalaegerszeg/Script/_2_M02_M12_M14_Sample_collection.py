from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__2_M02_M12_M14_Sample_collection(motor_config: MotorConfig):
    


    straight_speed = 700
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration = 120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)


       

    #indul a robot
    #elindulunk, cápával felszerelkezve
    drive_base.straight(distance=599)
    drive_base.turn(angle=-42.5)
    drive_base.use_gyro(False)
    drive_base.settings(1000, 1000, 500, 120)
    drive_base.straight(distance=245)
    drive_base.settings(1000, 1000, 500, 500)
    #felveszünk egy krillt, és a szigony alját 
    motor_config.a_motor.run_time(speed=-1000,time=385)
    drive_base.straight(distance=-90)
    motor_config.a_motor.run_time(speed=-1000, time=800)
    #hazahozzuk a
    drive_base.settings(1000,500,500,120)
    motor_config.a_motor.run_time(speed=1000,time=410)
    drive_base.curve(radius=-300, angle=-23)
    drive_base.straight(distance=-570)

    hub.light.on(Color.BLUE)
    wait(50000)
