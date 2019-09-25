from teacher import PiggyParent

class Piggy(PiggyParent):

    def __init__(self, *args, **kwargs):
        """Piggy constructor"""
        super().__init__(*args, **kwargs)

        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80

    def load_defaults(self):
        """Implements magic numbers defined in constructor"""
        
        self.set_motor_power(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_power(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
