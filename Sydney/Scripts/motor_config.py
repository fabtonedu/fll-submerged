from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction

class MotorConfig():
    def __init__(self, left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE), 
    right_motor = Motor(Port.D),
    a_motor = Motor(Port.A),
    b_motor = Motor(Port.B)):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.a_motor = a_motor
        self.b_motor = b_motor

motor_config = MotorConfig()