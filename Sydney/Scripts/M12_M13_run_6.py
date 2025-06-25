from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

"""
A radart maximalis pontra elforditjuk, majd letesszuk az osszes krillunket a balnaba, es hazamegyunk.
"""

def run__6_whale(motor_config: MotorConfig):
    


    straight_speed =600
    straight_acceleration = 250
    turn_rate = 500
    turn_acceleration =120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot
    #előremegzünk a bálnához
    drive_base.straight(710.8)
    drive_base.turn(38)
    drive_base.straight(123)
    wait(500)
    #beleeresztjük a krilleket a bálna szájába
    drive_base.straight(-145)
    #odamegyünk a kisebb hajóhoz hogy másik sávba tegyük
    drive_base.turn(-40)
    drive_base.straight(-100)
    #felemeljük a hajót, és másik sávba helyezzük
    drive_base.turn(-45)
    motor_config.b_motor.run_time(speed=-1000, time=2300)
    drive_base.straight(-132)
    motor_config.b_motor.run_time(speed=1000, time=2300)
    drive_base.straight(-150)
    #visszamegyünk a bázisra
    drive_base.straight(140)
    drive_base.settings(1000,1000,500,500)
    drive_base.turn(50)
    drive_base.straight(-600)
    
