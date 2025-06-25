from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__4_vessel(motor_config: MotorConfig):
    


    straight_speed =1000
    straight_acceleration =1000
    turn_rate = 500
    turn_acceleration =120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a program
    #előremegyünk és leüritjük a hajóba a mintákat és a ládát
    drive_base.settings(500, 500, 250, 250)
    drive_base.straight(650)
    drive_base.turn(-47)
    #betoljuk a cápát a megfelelő területre
    drive_base.settings(1000, 1000, 190, 190)
    drive_base.straight(240)
    #átmegyünk a másik bázisra
    drive_base.turn(50)
    drive_base.straight(1000)



