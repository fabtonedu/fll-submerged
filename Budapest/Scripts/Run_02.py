from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor,
UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port,
Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run_shark_M02(motor_config: MotorConfig):
    straight_speed = 1000
    straight_acceleration = 500
    turn_rate = 500
    turn_acceleration = 120
    drive_base = DriveBase(motor_config.left_motor,
    motor_config.right_motor, wheel_diameter=62, axle_track=180)
    
    #konfiguráljuk a “Drive Base”
    drive_base.settings(straight_speed, straight_acceleration,
    turn_rate,turn_acceleration)
    drive_base.use_gyro(True)
    
    
    # elindul a robot
    # a robot kiszabadítja a cápát
    drive_base.straight(distance=750)
    drive_base.turn(angle=-40)
    drive_base.straight(distance=70)
    
    # a robot odamegy a korallzátonyhoz
    drive_base.straight(distance=-70)
    drive_base.turn(angle=35)
    drive_base.straight(distance=100)
    drive_base.turn(angle=76)
    
    # a robot felfordítja a korall struktúrát
    motor_config.a_motor.run_time(350,1000)
    motor_config.a_motor.run_time(-350,1000)
    drive_base.turn(angle=35)
    
    # a robot odamegy a földmintához
    drive_base.straight(distance=300)
    drive_base.turn(angle=-65)
    
    # a robot kiemeli a földmintát
    motor_config.b_motor.run_time(speed=-395,time=955)
    drive_base.straight(distance=180)
    motor_config.b_motor.run_time(speed=110,time=1000)
    drive_base.straight(distance=-1000)
    hub.light.on(Color.BLACK)
    wait(50000)