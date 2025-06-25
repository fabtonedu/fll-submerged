from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# Importáld be a futásokat
from M05_M09_M14_run_1 import run__1_anglerfish
from M01_M02_M03_M04_M06_M07_run_2 import run__2_scuba
from M02_M14_run_3 import run__3_trident
from M15_run_4 import run__4_vessel
from M03_M08_run_5 import run__5_coralls
from M12_M13_run_6 import run__6_whale
from M09_M10_M11_run_7 import run__7_submersible

# Motor konfiguráció
from motor_config import motor_config, MotorConfig

hub = InventorHub()

# Menü gombok
menu_options = ("1", "2", "3", "4", "5", "6")
menu_index = 0


def run_program(selected: int):
    print("Running program:", selected)
    if selected == 1:
        run__1_anglerfish(motor_config=motor_config)
    elif selected == 2:
        run__2_scuba(motor_config=motor_config)
    elif selected == 3:
        run__3_trident(motor_config=motor_config)
    elif selected == 4:
        run__5_coralls(motor_config=motor_config)
    elif selected == 5:
        run__6_whale(motor_config=motor_config)
    elif selected == 6:
        run__6_whale(motor_config=motor_config)



# Végtelen ciklus: menü és futtatás
while True:
    print("Welcome to the robot menu!")
    hub.system.set_stop_button(None)

    while True:
        # Kijelzi az aktuális menüpontot
        hub.display.char(menu_options[menu_index])

        pressed = ()
        while len(pressed) == 0:
            pressed = hub.buttons.pressed()
            wait(10)

        while hub.buttons.pressed():
            wait(10)

        if Button.CENTER in pressed:
            break
        elif Button.LEFT in pressed:
            menu_index = (menu_index - 1) % len(menu_options)
        elif Button.RIGHT in pressed:
            menu_index = (menu_index + 1) % len(menu_options)

    hub.system.set_stop_button(Button.CENTER)

    selected = int(menu_options[menu_index])

    try:
        run_program(selected=selected)
        pressed = ()
    except SystemExit:
        # Motorok leállítása és újrainicializálása hiba esetén
        motor_config.left_motor.close()
        motor_config.right_motor.close()
        motor_config.a_motor.close()
        motor_config.b_motor.close()

        while not hub.imu.ready():
            wait(50)

        hub.display.text("X")
        wait(1000)

        # Újra inicializáljuk a motor_config-ot
        motor_config = MotorConfig(
            left_motor=Motor(Port.C, Direction.COUNTERCLOCKWISE),
            right_motor=Motor(Port.D),
            a_motor=Motor(Port.A),
            b_motor=Motor(Port.B)
        )
