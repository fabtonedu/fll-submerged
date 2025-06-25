from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()


def run__1_M01_M02_M03_M04_M06_Scuba_diver(motor_config: MotorConfig):
    


    straight_speed = 500
    straight_acceleration = 250
    turn_rate = 500
    turn_acceleration = 120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot
    drive_base.settings(1000, 500, 500, 120)
    drive_base.straight(distance=-190)
    drive_base.turn(angle=38)
    #begyűjtünk egy korallt, a vizmintát és egy krillt
    drive_base.straight(distance=-580)
    drive_base.straight(distance=80)
    #hátratolatunk, leemeljük a búvárt és benyomjuk a korallokat
    drive_base.turn(angle=50)
    drive_base.settings(500,500,500,120)
    motor_config.b_motor.run_time(speed=-1000, time=670)
    wait(500)
    drive_base.settings(500,500,500,120)
    drive_base.straight(distance=120)
    drive_base.settings(1000,500,500,120)
    wait(50)
    motor_config.b_motor.run_time(speed=250, time=400)
    #hátramegyünk és felemeljük az árbócot
    wait(50)
    drive_base.straight(distance=-30)
    drive_base.settings(60, 500, 500, 120)
    drive_base.curve(radius=-2000, angle=10)
    drive_base.turn(angle=20)
    #ráfordulunk a cápára, és leengedjük
    drive_base.settings(1000, 500 , 500 , 120)
    drive_base.curve( radius=1550 , angle=15.6)
    #rámozdulunk a búvárra, hogy lerakhassuk 
    drive_base.straight(distance=-23)
    drive_base.turn(angle=60)
    drive_base.straight(distance=-150.5)
    drive_base.turn(angle=34.7)
    drive_base.straight(distance=120)
    motor_config.b_motor.run_time(speed=-200, time=550)
    #lenzomjuk a korallszirteket
    drive_base.straight(distance=-130)
    motor_config.b_motor.run_time(speed=-800, time=50)
    drive_base.turn(angle=-1.5)
    drive_base.straight(distance=100)
    motor_config.b_motor.run_time(speed=-400, time=1000)
    motor_config.b_motor.run_time(speed=400, time=1000)
    #begyűjtjük a korallt és hazajövünk
    drive_base.turn(angle=-40)
    drive_base.curve(radius=-500 ,angle=-80)
    hub.light.on(Color.BLUE)
    wait(time=50000)


 
