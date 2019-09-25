#!/usr/bin/env python
# Based on:
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This code is an example for controlling the GoPiGo3 Motors
#
# Results:  When you run this program, manually rotate the left motor to control the speed of the right motor.
import gopigo3, sys

class PiggyParent(gopigo3.GoPiGo3):
    def __init__(self, addr=8, detect=True):
        super().__init__(addr=addr, detect=detect)
        if sys.version_info < (3, 0):
            sys.stdout.write("Sorry, requires Python 3.x\n")
            self.quit()

    def deg_fwd(self, deg):
        """Zeroes current encorder values then moves forward based on degrees given"""
        self.offset_motor_encoder(self.MOTOR_LEFT, self.get_motor_encoder(self.MOTOR_LEFT))
        self.offset_motor_encoder(self.MOTOR_RIGHT, self.get_motor_encoder(self.MOTOR_RIGHT))
        self.set_motor_position(self.MOTOR_LEFT + self.MOTOR_RIGHT, deg)

    def fwd(self):
        self.set_motor_power(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_power(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)

    def quit(self):
        """Terminates robot movement and settings then closes app"""
        print("\nIt's been a pleasure.\n")
        self.reset_all()
        sys.exit(1)