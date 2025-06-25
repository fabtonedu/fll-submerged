from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__4_M03_M11_M12_M14_Sonar_discovery(motor_config: MotorConfig):
    


    straight_speed = 700
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration =120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot
    drive_base.curve(radius=-500, angle=35)
    drive_base.turn(angle=38)
    #begyűjtünk két krillt
    drive_base.curve(radius=-950, angle=25)
    drive_base.turn(angle=70)
    #ráfordulunk a planktonmintára és összeszedjük
    drive_base.curve(radius=-180, angle=-48.8)
    drive_base.straight(distance=60)  
    drive_base.turn(angle=-22)
    drive_base.straight(distance=88)
    #a szonárt teljesen körbeforgassuk
    motor_config.b_motor.run_time(speed=-700, time=1600)
    motor_config.b_motor.run_time(speed=700, time=630.00)
    wait(50)   
    #hazamanőverezik a robot
    drive_base.straight(distance=-40)
    motor_config.b_motor.run_time(speed=700, time=100.00)
    drive_base.turn(angle=-93)
    drive_base.straight(distance=800)
    hub.light.on(Color.BLUE)
    wait(50000)


