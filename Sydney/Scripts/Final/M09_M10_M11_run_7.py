from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = InventorHub()


def setup_drive_base(motor_config):
    drive_base = DriveBase(
        motor_config.left_motor,
        motor_config.right_motor,
        wheel_diameter=62,
        axle_track=180
    )
    drive_base.use_gyro(True)
    drive_base.settings(700, 500, 500, 120)
    return drive_base


# Mission 11: Sonar Discovery – forgatás a bálnák felfedéséhez
def activate_sonar(drive_base, motor_config):
    drive_base.straight(500)
    drive_base.turn(-39)
    drive_base.straight(330)
    motor_config.b_motor.run_time(speed=-1000, time=1340)
    wait(100)
    drive_base.straight(10)


# Mission 10: Submersible – tengeralattjáró átküldése
def launch_submersible(drive_base, motor_config):
    wait(400)
    drive_base.straight(-150)
    drive_base.turn(-14)
    motor_config.a_motor.run_time(speed=1000, time=800)
    drive_base.straight(448)
    motor_config.a_motor.run_time(speed=-1000, time=900)
    wait(1500)


# Mission 9: Unexpected Encounter – lény eljuttatása a hideg zónába
def deliver_unknown_creature(drive_base, motor_config):
    motor_config.a_motor.run_time(speed=1000, time=600)
    drive_base.straight(-100)
    drive_base.turn(-60)
    drive_base.straight(200)


def run__7_submersible(motor_config):
    drive_base = setup_drive_base(motor_config)

    activate_sonar(drive_base, motor_config)
    launch_submersible(drive_base, motor_config)
    deliver_unknown_creature(drive_base, motor_config)
