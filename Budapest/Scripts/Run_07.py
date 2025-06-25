from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor,
UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,
Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = InventorHub()


"""
A radart maximális pontra elforditjuk, majd letesszük az összes
krillet a bálnába, és hazamegyünk.
"""


def run_sonar_discovery_M11_M12(motor_config: MotorConfig):
    straight_speed =700
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration =120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    
    #konfiguráljuk a “Drive Base”
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    
    #indul a robot
    """
    Fontos odafigyelni, hogy a beállításnál fejjel lefelé helyezzük be a
    krilleket.
    """
    #megközelítjük a radart
    drive_base.curve(radius=290, angle=90)
    drive_base.straight(distance=350)
    
    #befordulunk a radarhoz
    drive_base.turn(15)
    
    #giroszkóp kikapcsolása a radar forgatásához
    drive_base.use_gyro(False)
    motor_config.a_motor.run_time(speed=-1000, time=1300)
    
    #visszahozzuk a kart, kitolatunk
    drive_base.use_gyro(True)
    motor_config.a_motor.run_time(speed=1000, time=700)
    
    #elmegyunk a radartól
    drive_base.curve(radius=-400, angle=-30.5)
    
    #kinyitjuk a bálna száját
    drive_base.use_gyro(False)
    drive_base.straight(distance=260)
    drive_base.straight(distance=-30)
    
    #bele ürítjük a dolg
    drive_base.straight(distance=45)
    wait(time=500)
    drive_base.use_gyro(True)
    
    #hazamegyünk a bázisra
    drive_base.curve(radius=-340, angle=110)
    drive_base.settings(700, 500, 1000, 120)
    drive_base.straight(distance=-300)
    hub.light.on(Color.BLACK)
    wait(time=50000)
