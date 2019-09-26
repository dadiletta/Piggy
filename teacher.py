# PYTHON3 ONLY
# Based on:
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md

import gopigo3, sys
from di_sensors.easy_distance_sensor import EasyDistanceSensor

class PiggyParent(gopigo3.GoPiGo3):

    '''
    UTILITIES
    '''

    def __init__(self, addr=8, detect=True):
        gopigo3.GoPiGo3.__init__(self)
        self.scan = []
        self.distance_sensor = EasyDistanceSensor()

    def calibrate(self):
        pass

    def quit(self):
        """Terminates robot movement and settings then closes app"""
        print("\nIt's been a pleasure.\n")
        self.reset_all()
        sys.exit(1)

    '''
    MOVEMENT
    '''

    def deg_fwd(self, deg):
        """Zeroes current encorder values then moves forward based on degrees given"""
        self.offset_motor_encoder(self.MOTOR_LEFT, self.get_motor_encoder(self.MOTOR_LEFT))
        self.offset_motor_encoder(self.MOTOR_RIGHT, self.get_motor_encoder(self.MOTOR_RIGHT))
        self.set_motor_position(self.MOTOR_LEFT + self.MOTOR_RIGHT, deg)

    def fwd(self, left=self.LEFT_DEFAULT, right=self.RIGHT_DEFAULT):
        """Blindly charges your robot forward at default power which needs to be configured in child class"""
        self.set_motor_power(self.MOTOR_LEFT, left)
        self.set_motor_power(self.MOTOR_RIGHT, right)

    def right(self, primary=90, counter=0):
        """Rotates right by powering the left motor to default"""
        self.set_motor_power(self.MOTOR_LEFT, primary)
        self.set_motor_power(self.MOTOR_RIGHT, counter)

    def left(self, primary=90, counter=0):
        """Rotates left by powering the left motor to 90 by default and counter motion 0"""
        self.set_motor_power(self.MOTOR_LEFT, counter)
        self.set_motor_power(self.MOTOR_RIGHT, primary)      

    def back(self, left=-self.LEFT_DEFAULT, right=-self.RIGHT_DEFAULT):
        self.set_motor_power(self.MOTOR_LEFT, left)
        self.set_motor_power(self.MOTOR_RIGHT, right)

    '''
    SENSORS
    '''

    def read_distance(self):
        """Returns the GoPiGo3's distance sensor in MM over IC2"""
        d = self.distance_sensor.read_mm()
        print(f"Distance Sensor Reading: {d} mm ")
        return d
