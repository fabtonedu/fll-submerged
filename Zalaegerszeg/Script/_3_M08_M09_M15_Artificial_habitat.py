from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__3_M08_M09_M15_Artificial_habitat(motor_config: MotorConfig):
    


    straight_speed =1000
    straight_acceleration = 2000
    turn_rate = 500
    turn_acceleration =120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a program
    #passziv karral előrenyomjuk a hajót valameddig
    drive_base.straight(distance=795)   
    drive_base.settings(50, 2000, 500, 120)
    drive_base.turn(angle=-4.5)
    drive_base.straight(distance=145)
    #felhúzzuk a mesterséges élőhelyet
    drive_base.straight(distance=-190)
    drive_base.settings(1000, 1000, 500, 120)
    drive_base.turn(angle=-135)
    drive_base.straight(distance=-200)
    drive_base.turn(angle=-23)
    drive_base.use_gyro(False)
    #betoljuk a hajót a helyére
    drive_base.straight(distance=-265)
    drive_base.straight(distance=310)
    #kijövünk a hajó és a mesterséges élőhely közül
    drive_base.use_gyro(True)
    drive_base.turn(angle=70)
    #drive_base.straight(distance=90)
    #drive_base.straight(165)
    #drive_base.turn(48)
    drive_base.straight(60)
    drive_base.curve(radius=158, angle=55)
    #drive_base.turn(20)
    drive_base.straight(distance=100)
    drive_base.curve(radius=120, angle=55)
    #drive_base.turn(40)
    drive_base.straight(500)
    drive_base.curve(radius=112, angle=33)
    drive_base.settings(500,2000, 500, 120)
    #kiengedjük az ismertlen lényt, összegyűjtjük, és hazamegyünk
    drive_base.straight(distance=-345)
    #drive_base.turn(angle=2)
    drive_base.settings(500, 2000, 500, 120)
    drive_base.straight(430)



    hub.light.on(Color.BLACK)
    wait(time=50000)


