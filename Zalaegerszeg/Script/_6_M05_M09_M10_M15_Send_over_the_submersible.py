from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

def run__6_M05_M09_M10_M15_Send_over_the_submersible(motor_config: MotorConfig):
    


    straight_speed =700
    straight_acceleration = 1000
    turn_rate = 500
    turn_acceleration =120


    drive_base = DriveBase(motor_config.left_motor, motor_config.right_motor, wheel_diameter=62, axle_track=180)

    #configure drive base 
    drive_base.settings(straight_speed, straight_acceleration, turn_rate,turn_acceleration)
    drive_base.use_gyro(True)

    #indul a robot
    drive_base.straight(distance=500)
    drive_base.turn(angle=-18) 
    #a hajót megtöltjük két mintával és a szigony felső felével
    motor_config.a_motor.run_time(speed=700, time=450)
    wait(100)
    motor_config.a_motor.run_time(speed=-700, time=450)
    #előremegyünk és kicsaloatjuk az ördöghalat a helyéről
    drive_base.turn(angle=16.8)
    drive_base.straight(distance=-50)
    drive_base.turn(angle=46.2)
    drive_base.straight(distance=700)
    drive_base.straight(distance=-25)
    drive_base.turn(angle=115)
    #ráfordulunk a tengeralattjáróra 
    drive_base.straight(distance=260)
    drive_base.turn(angle=-110)
    drive_base.straight(distance=65)
    #átküldjük a tengeralattjárót az ellenfél térfelére
    motor_config.b_motor.run_time(speed=1000, time=540)
    wait(1000)
    motor_config.b_motor.run_time(speed=1000, time=200)
    drive_base.straight(distance=-80)
    hub.light.on(Color.BLUE)
    wait(time=50000)




