from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = InventorHub()


def setup_drive_base(motor_config):
    # Meghajtás beállítása és giroszkóp aktiválása
    drive_base = DriveBase(
        motor_config.left_motor,
        motor_config.right_motor,
        wheel_diameter=62,
        axle_track=180
    )
    drive_base.use_gyro(True)
    drive_base.settings(600, 250, 500, 120)
    return drive_base


# 🐋 Mission 12: Feed the Whale – Etessük meg a bálnát krillekkel
def feed_the_whale(drive_base):
    drive_base.straight(710.8)
    drive_base.turn(38)
    drive_base.straight(123)
    wait(500)
    drive_base.straight(-145)


# 🚢 Mission 13: Change Shipping Lane – Mozgassuk át a hajót másik sávba
def move_cargo_ship(drive_base, motor_config):
    drive_base.turn(-40)
    drive_base.straight(-100)
    drive_base.turn(-45)
    # Emeljük fel a hajót
    motor_config.b_motor.run_time(speed=-1000, time=2300)
    # Toljuk új helyre
    drive_base.straight(-132)
    # Engedjük vissza
    motor_config.b_motor.run_time(speed=1000, time=2300)
    # Haladjunk tovább
    drive_base.straight(-150)


# ⛳ Zárás: visszatérés a bázisra
def return_home(drive_base):
    drive_base.straight(140)
    drive_base.settings(1000, 1000, 500, 500)
    drive_base.turn(50)
    drive_base.straight(-600)


def run__6_whale(motor_config):
    drive_base = setup_drive_base(motor_config)

    feed_the_whale(drive_base)
    move_cargo_ship(drive_base, motor_config)
    return_home(drive_base)
