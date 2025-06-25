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
    drive_base.settings(1000, 500, 250, 250)
    return drive_base


# 🐙 Mission 9: Unexpected Encounter – ismeretlen lény begyűjtése
def collect_unknown_creature(drive_base):
    drive_base.straight(-170)
    drive_base.turn(-40)
    drive_base.straight(-290)
    wait(50)
    drive_base.straight(144)


# 🧫 Mission 14: Sample Collection – minták, korall, krillek begyűjtése
def collect_samples_and_krill(drive_base):
    drive_base.turn(35.5)
    drive_base.straight(-270)
    drive_base.curve(radius=-230, angle=12)
    drive_base.straight(-40)
    drive_base.turn(60)
    drive_base.straight(-30)
    drive_base.curve(radius=-100, angle=-30)
    drive_base.straight(-80)
    wait(50)
    drive_base.straight(200)
    drive_base.turn(48.5)


# 🐟 Mission 5: Anglerfish – betoljuk a horgászhalat a helyére
def push_anglerfish(drive_base):
    drive_base.curve(radius=900, angle=-30)
    drive_base.turn(81)
    wait(50)
    drive_base.turn(77)


# ➕ További minták és korall begyűjtése
def collect_more_samples(drive_base):
    drive_base.straight(-100)
    wait(50)
    drive_base.turn(54.5)
    drive_base.straight(-279)
    drive_base.turn(-54.5)
    drive_base.straight(-300)
    drive_base.curve(radius=-262, angle=22.5)
    drive_base.turn(-26.5)
    drive_base.straight(-600)


def run__1_anglerfish(motor_config):
    drive_base = setup_drive_base(motor_config)

    collect_unknown_creature(drive_base)
    collect_samples_and_krill(drive_base)
    push_anglerfish(drive_base)
    collect_more_samples(drive_base)
