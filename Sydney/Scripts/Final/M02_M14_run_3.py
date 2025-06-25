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
    drive_base.settings(1000, 1000, 500, 120)
    return drive_base


# 🦈 Mission 2: Shark – eljuttatjuk a cápát az új helyére
def guide_shark_to_habitat(drive_base, motor_config):
    drive_base.straight(430)
    drive_base.turn(-39)
    drive_base.straight(400)
    motor_config.b_motor.run_time(speed=-1000, time=1340)
    wait(100)
    drive_base.straight(10)
    wait(400)


# ⚔️ Mission 14: Trident – kivesszük a szigonydarabokat a roncsból
def retrieve_trident_parts(drive_base, motor_config):
    drive_base.straight(-150)
    drive_base.turn(-14)
    motor_config.a_motor.run_time(speed=1000, time=800)
    drive_base.straight(448)
    motor_config.a_motor.run_time(speed=-1000, time=900)
    wait(1500)
    motor_config.a_motor.run_time(speed=1000, time=600)
    drive_base.straight(-100)
    drive_base.turn(-60)
    drive_base.straight(200)


def run__3_trident(motor_config):
    drive_base = setup_drive_base(motor_config)

    guide_shark_to_habitat(drive_base, motor_config)
    retrieve_trident_parts(drive_base, motor_config)