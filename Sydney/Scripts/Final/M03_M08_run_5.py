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
    drive_base.settings(1000, 500, 500, 500)
    return drive_base


# 🦀 Mission 8: Artificial Habitat – rák-ketrecek beállítása
def handle_crab_traps(drive_base):
    drive_base.curve(radius=3800, angle=10)
    wait(100)
    drive_base.settings(1000, 1000, 500, 500)
    wait(100)
    drive_base.turn(-5)
    drive_base.straight(600)


# 🪸 Mission 3: Coral Reef – korallok leengedése és felállítása
def deploy_coral_structure(drive_base, motor_config):
    drive_base.settings(1000, 500, 250, 250)
    motor_config.a_motor.run_time(speed=-400, time=500)
    wait(50)
    drive_base.straight(-100)


# 🏁 Visszatérés a bázisra
def return_to_base(drive_base):
    drive_base.turn(-26)
    drive_base.curve(radius=-1600, angle=-17)
    drive_base.straight(-300)
    drive_base.curve(radius=-200, angle=-70)
    drive_base.straight(-200)


def run__5_coralls(motor_config):
    drive_base = setup_drive_base(motor_config)

    handle_crab_traps(drive_base)
    deploy_coral_structure(drive_base, motor_config)
    return_to_base(drive_base)