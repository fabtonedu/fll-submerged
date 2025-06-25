from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = InventorHub()



def run_send_over_the_submersible_M10(motor_config: MotorConfig):
    straight_speed =700
    straight_acceleration = 1000
    turn_rate = 500
    turn_acceleration =120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    #konfiguraljuk a drive baset
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    
    #indul a robot
    #lerakjuk az ismeretlen lenyt
    #mesterséges élőhelyeket talpra állitja a robot
    drive_base.straight(distance=600)
    motor_config.a_motor.run_time(speed=2000, time=2000)
    drive_base.turn(angle=60)
    
    #körbekerüljük a süllyedt hajót, valamint visszakergetjük a
    horgászhalat a rejtekhelyébe
    
    #a bal oldali A kart leengedjük, hogy ne akadjon bele a
    körölöttünk levő akadályokba
    motor_config.a_motor.run_time(speed=-1000, time=750)
    drive_base.straight(distance=290)
    drive_base.curve(radius=260, angle=-57)
    drive_base.turn(angle=20)
    
    #a tengeralattjárót átküldjük az ellenfél térfelére
    drive_base.straight(distance=-200)
    drive_base.turn(angle=65)
    motor_config.a_motor.run_time(speed=-500, time=800)
    drive_base.settings(1000, 1000, 500, 120)
    drive_base.straight(distance=200)
    drive_base.turn(angle=20)
    
    #itt fenntartjuk egy ideig a tengeralattjárót, és az ismeretlen
    lény pont a mély tenger fölé kerül
    motor_config.a_motor.run_time(speed=800, time=700,
    wait=False)
    wait(time=3000)
    motor_config.a_motor.run_time(speed=-300, time=1000)
    drive_base.turn(angle=-20)
    motor_config.b_motor.run_time(speed=300, time=20000)
    hub.light.on(Color.BLACK)
    wait(time=50000)
