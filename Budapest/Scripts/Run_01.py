from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = InventorHub()
def run_coral_nursery_M01(motor_config: MotorConfig):
    straight_speed = 500
    straight_acceleration = 250
    turn_rate = 500
    turn_acceleration = 120
    
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    # konfiguráljuk a “drive base”

    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    # a robot felszedi a korall szegmens
    drive_base.curve(radius=-270, angle=110)
    drive_base.straight(distance=-130)
    drive_base.straight(distance=100)
    
    # a robot felveszi a krillt
    drive_base.turn(angle=20)
    drive_base.straight(distance=-180)
    
    # a robot a vízmintát
    drive_base.straight(distance=240)
    drive_base.turn(angle=25)
    drive_base.straight(distance=-100)
    drive_base.curve(radius=-600, angle=-30)
    
    # a robot felfordítja a korlat
    drive_base.curve(radius=280, angle=30)
    drive_base.use_gyro(False)
    drive_base.straight(distance=175)
    
    # a robot leveszi a búvárt
    motor_config.b_motor.run_time(speed=100, time=800)
    drive_base.use_gyro(True)
    drive_base.straight(distance=-60)
    
    # a robot felakasztja a búvárt a helyére
    drive_base.turn(angle=108)
    drive_base.straight(distance=50)
    motor_config.b_motor.run_time(speed=-500, time=700)
    
    # a robot hazamegy
    drive_base.curve(radius=-800, angle=-70)
    hub.light.on(Color.BLACK)
    wait(time=50000)