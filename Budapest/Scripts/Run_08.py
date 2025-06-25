from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor,
UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,
Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()


def run_vessel(motor_config: MotorConfig):
    straight_speed = 900
    straight_acceleration = 800
    turn_rate = 500
    turn_acceleration = 120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    #configure drive base
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    #indul a robot
    #berakjuk a hajoba az osszegyujtott mintakat, valamint a szigonyrészeit
    
    drive_base.straight(distance=360)
    drive_base.turn(angle=60)
    drive_base.straight(-30)
    drive_base.turn(angle=-60)
    
    #eltoljuk eközben a mesterséges élőhely egyik felét
    drive_base.straight(130)
    
    #itt beleejtjük az összeszedett mintákat és a szigony részeket
    motor_config.a_motor.run_time(speed=200, time=1000)
    wait(1000)
    motor_config.a_motor.run_time(speed=-1000, time=600)
    
    #a mesterséges élőhelyeket tökéletesen egymáshoz illesztjük, és hazatolatunk
    drive_base.settings(999, 500, 500, 120)
    drive_base.straight(-120)
    drive_base.turn(20)
    drive_base.straight(120)
    drive_base.straight(distance=-500)
    hub.light.on(Color.BLACK)
    wait(time=50000)