from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from _1_M01_M02_M03_M04_M06_Scuba_diver import run__1_M01_M02_M03_M04_M06_Scuba_diver
from _2_M02_M12_M14_Sample_collection import run__2_M02_M12_M14_Sample_collection
from _3_M08_M09_M15_Artificial_habitat import run__3_M08_M09_M15_Artificial_habitat
from _4_M03_M11_M12_M14_Sonar_discovery import run__4_M03_M11_M12_M14_Sonar_discovery
from _5_M12_Feed_the_whale import run__5_M12_Feed_the_whale
from _6_M05_M09_M10_M15_Send_over_the_submersible import run__6_M05_M09_M10_M15_Send_over_the_submersible
from _7_M03_Coral_reef import run_coralls
from _8_csere_M05_M09_M10_M15_Send_over_the_submersible import run__8_M05_M09_M10_M15_Send_over_the_submersible

from motor_config import motor_config, MotorConfig


def init_motor_conf():
    motor_config= MotorConfig(
        left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE),
        right_motor = Motor(Port.D),
        a_motor = Motor(Port.A),
        b_motor = Motor(Port.B),
        )


# Let's offer these menu options. You can add as many as you like.
menu_options = ("1", "2", "3", "4", "5", "6" , "7", "8")
menu_index = 0

hub = InventorHub()


def run_program(selected: int):
    print("running program: " + str(selected))
    if selected == 1:      
        run__1_M01_M02_M03_M04_M06_Scuba_diver(motor_config=motor_config)
    elif selected == 2:
        run__2_M02_M12_M14_Sample_collection(motor_config=motor_config)
    elif selected == 3:
        run__3_M08_M09_M15_Artificial_habitat(motor_config=motor_config)
    elif selected == 4:
        run__4_M03_M11_M12_M14_Sonar_discovery(motor_config=motor_config)
    elif selected == 5:
        run__5_M12_Feed_the_whale(motor_config=motor_config)
    elif selected == 6:
        run_coralls(motor_config=motor_config)
    elif selected == 7:
        run__6_M05_M09_M10_M15_Send_over_the_submersible(motor_config=motor_config)
    elif selected == 8:
        run__8_M05_M09_M10_M15_Send_over_the_submersible(motor_config=motor_config)

while True:

    # Normally, the center button stops the program. But we want to use the
    # center button for our menu. So we can disable the stop button.
    print("Hello to menu")
    hub.system.set_stop_button(None)

    while True:

        hub.display.char(menu_options[menu_index])

        # Wait for any button.
        pressed = ()
        while len(pressed) == 0:
            pressed = hub.buttons.pressed()
            wait(10)

            # Wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)

            # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, so the menu is done!
            break
        elif Button.LEFT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index = (menu_index - 1) % len(menu_options)
        elif Button.RIGHT in pressed:
            # Right button, so increment menu menu_index.
            menu_index = (menu_index + 1) % len(menu_options)

    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)

    # Based on the selection, choose a program.
    selected = int(menu_options[menu_index])

    try:
        run_program(selected=selected)
        pressed = ()
    except SystemExit as ex:
        motor_config.left_motor.close()
        # global right_motor
        motor_config.right_motor.close()
        # global a_motor
        motor_config.a_motor.close()
        # global b_motor
        motor_config.b_motor.close()
        print(hub.imu.ready())
        while not hub.imu.ready():
            wait(50)
        hub.display.text("X")
        #hub.color.on(Color.BLUE)
        init_motor_conf()
        
        