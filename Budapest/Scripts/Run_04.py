from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor,
UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,
Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = InventorHub()


def run_sample_collection_M12(motor_config: MotorConfig):
    straight_speed = 700
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration = 120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    # konfiguráljuk a “Drive Base”
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    # elindul a robot
    # odamegy a robot a szigonyhoz
    # a robot lerakja a cápát az új táplálék forráshoz
    drive_base.straight(distance=100)
    drive_base.curve(radius=880, angle=-44)
    
    # a robot felveszi a krillt
    drive_base.straight(distance=50)
    drive_base.straight(distance=-38)
    
    # a robot kiveszi a szigonyt
    drive_base.use_gyro(False)
    motor_config.a_motor.run_time(speed=-999, time=2000)
    drive_base.use_gyro(True)
    motor_config.a_motor.run_time(speed=500, time=350)
    motor_config.a_motor.run_time(speed=200, time=1500)
    drive_base.straight(distance=-200)
    drive_base.turn(angle=40)
    drive_base.straight(distance=-600)
    hub.light.on(Color.BLACK)
    wait(time=50000)