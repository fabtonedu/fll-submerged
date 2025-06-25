from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run_coralls(motor_config: MotorConfig):
    


    straight_speed = 300
    straight_acceleration = 200
    turn_rate = 500
    turn_acceleration = 120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)


    #indul a robot
    #kitoljuk a korallokat és hazajövünk
    drive_base.straight(distance=50)
    drive_base.straight(distance=-50)
    hub.light.on(Color.BLUE)
    wait(time=50000)





