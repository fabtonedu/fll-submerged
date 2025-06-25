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
    drive_base.settings(700, 600, 250, 120)
    return drive_base


# 🚗 Kihajtás a bázisról - 
def leave_base(drive_base):
    drive_base.straight(-60)
    drive_base.turn(42)
    drive_base.straight(-380)
    drive_base.turn(47)


# 🚢 M06 & M07 – Hajóroncs felállítása és láda kimentése
def raise_mast_and_retrieve_chest(drive_base):
    drive_base.settings(550, 450, 500, 120)
    drive_base.straight(-300)
    wait(50)
    drive_base.straight(120)
    drive_base.settings(700, 600, 500, 120)
    drive_base.turn(78)
    drive_base.straight(122)
    drive_base.turn(-72)


# 🤿 M01 & M04 – Korallfa és búvár manipuláció
def coral_tree_and_diver(drive_base, motor_config):
    motor_config.a_motor.run_time(speed=-999, time=830)
    drive_base.settings(200, 150, 500, 120)
    motor_config.b_motor.run_time(speed=-300, time=680)
    drive_base.straight(105)
    motor_config.a_motor.run_time(200, 2125)
    motor_config.a_motor.run_time(-200, 800)
    motor_config.b_motor.run_time(speed=800, time=350)
    wait(100)
    drive_base.straight(-60)


# 🪸 M03 – Búvár átjuttatása a korallokra
def move_diver_to_reef(drive_base, motor_config):
    drive_base.curve(radius=-90, angle=-81)
    drive_base.straight(92)
    motor_config.b_motor.run_time(-400, 340)
    wait(100)
    drive_base.straight(-70)
    drive_base.turn(-0.7)


# 🌿 M01 folytatás – Korallkert aktiválása
def activate_coral_garden(drive_base, motor_config):
    drive_base.settings(300, 300, 150, 150)
    motor_config.b_motor.run_time(1000, 700)
    drive_base.straight(68)
    wait(100)


# 🦈 M02 – Cápa elengedése
def release_shark(drive_base, motor_config):
    motor_config.b_motor.run_time(-1000, 900)
    wait(200)
    motor_config.b_motor.run_time(1000, 100)
    drive_base.turn(-5)
    motor_config.b_motor.run_time(1000, 700)


# 🏁 Visszatérés a bázisra
def return_to_base(drive_base, motor_config):
    drive_base.straight(-30)
    drive_base.turn(-50)
    drive_base.straight(77)
    motor_config.b_motor.run_time(speed=-1000, time=1000)
    motor_config.b_motor.run_time(speed=1000, time=1000)
    drive_base.settings(900, 900, 250, 250)
    drive_base.curve(radius=-100, angle=-85.0)
    drive_base.straight(-600)


def run__2_scuba(motor_config):
    drive_base = setup_drive_base(motor_config)

    leave_base(drive_base)
    raise_mast_and_retrieve_chest(drive_base)
    coral_tree_and_diver(drive_base, motor_config)
    move_diver_to_reef(drive_base, motor_config)
    activate_coral_garden(drive_base, motor_config)
    release_shark(drive_base, motor_config)
    return_to_base(drive_base, motor_config)
