from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor,
UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,
Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run_artificial_habitat_M15_M08(motor_config: MotorConfig):
    straight_speed = 900
    straight_acceleration = 900
    turn_rate = 500
    turn_acceleration = 120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    #konfiguráljuk a “Drive Base”
    
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    # elindul a robot
    # a robot eltolja a hajót
    drive_base.straight(distance=-700)
    drive_base.turn(angle=-140)
    drive_base.straight(distance=100)
    drive_base.turn(angle=-14)
    drive_base.use_gyro(False)
    drive_base.straight(distance=230)
    drive_base.use_gyro(True)
    drive_base.straight(distance=-120)
    drive_base.turn(angle=20)
    drive_base.straight(distance=-300)
    drive_base.turn(angle=-32)
    drive_base.straight(900)
    drive_base.turn(36)
    drive_base.straight(-150)
    drive_base.straight(600)
    drive_base.turn(60)
    hub.light.on(Color.BLACK)
    wait(time=50000)
