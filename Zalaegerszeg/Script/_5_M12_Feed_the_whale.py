from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

"""
A radart maximalis pontra elforditjuk, majd letesszuk az osszes krillunket a balnaba, es hazamegyunk.
"""

def run__5_M12_Feed_the_whale(motor_config: MotorConfig):
    


    straight_speed =1000
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration =120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot

    #indul a robot
    #előrejövünk és ráfordulunk a bálnára
    drive_base.straight(distance=760)
    #megetetjük a bálnát krillekkel
    drive_base.turn (angle=46.0)
    drive_base.straight(distance=114)
    wait(1200)
    #hátratolatunk a bálnából
    drive_base.straight(distance=-120.8)
    drive_base.curve(radius=-90,angle=-86.6)  
    drive_base.straight(distance=155)
    #felemeljük a ladikot
    motor_config.a_motor.run_time(speed=500, time=480)
    drive_base.settings(200,500,500,120)
    drive_base.straight(distance=140)
    motor_config.a_motor.run_time(speed=-500, time=400)
    drive_base.settings(1000,1000,500,120)
    #visszamgyünk a bázisra
    drive_base.straight(distance=-200)
    drive_base.turn(angle=30.9)
    drive_base.straight(distance=580)
    hub.light.on(Color.BLUE)
    wait(time=50000)





