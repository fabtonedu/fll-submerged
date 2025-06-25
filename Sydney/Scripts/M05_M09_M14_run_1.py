from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__1_anglerfish(motor_config: MotorConfig):
    


    straight_speed = 1000
    straight_acceleration = 500
    turn_rate = 250
    turn_acceleration = 250


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)


    #indul a robot
    #begyűjtjük az ismeretlen lényt
    drive_base.straight(-170)
    drive_base.turn(-40)
    drive_base.straight(-290)
    wait(50)
    drive_base.straight(144)
    #begyűjtünk még 3 krillt, és egy mintát
    drive_base.turn(35.5)
    drive_base.straight(-270)
    drive_base.curve(radius=-230,angle=12)
    drive_base.straight(-40)
    drive_base.turn(60)
    drive_base.straight(-30)
    drive_base.curve(radius=-100, angle=-30)
    drive_base.straight(-80)
    wait(50)
    drive_base.straight(200)
    drive_base.turn(48.5)
    #odamegyünk a horgászhalhoz és betoljuk a megfelelő helyre
    drive_base.curve(radius=900, angle=-30)
    drive_base.turn(81)
    wait(50)
    drive_base.turn(77)
    #odamegyünk a tengerfenékmintához és begyűjtjük azt is
    drive_base.straight(-100)
    wait(50)
    #begyűjtünk további két korallt, az utolsó mintát, és egy krillt
    drive_base.turn(54.5)
    drive_base.straight(-279)
    drive_base.turn(-54.5)
    drive_base.straight(-300)
    drive_base.curve(radius=-262, angle=22.5)
    drive_base.turn(-26.5)
    drive_base.straight(-600)

