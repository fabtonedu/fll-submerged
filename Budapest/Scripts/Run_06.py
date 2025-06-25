from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor,
UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,
Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = InventorHub()


def run_sample_collection_M14(motor_config: MotorConfig):
    straight_speed = 700
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration =120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    #konfiguráljuk a “Drive Base”
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    #elindul a robot
    drive_base.straight(distance=-100)
    drive_base.turn(angle=-20)
    drive_base.straight(distance=-230)
    # a robot begyűjt két krillt
    drive_base.turn(angle=30)
    drive_base.curve(radius=-480, angle=50 )
    # a robot begyűjti a korall mintát
    drive_base.straight(distance=100)
    drive_base.turn(angle=60)
    drive_base.curve(radius=-160, angle=-73)
    # a robot begyűjti a plankton mintát
    drive_base.settings(350, 500, 500, 120)
    drive_base.curve(radius=200, angle=-110)
    drive_base.straight(800)
    hub.light.on(Color.BLACK)
    wait(50000)
