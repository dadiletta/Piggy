# Piggy
#### Your maze navigating GoPiGo3

## Teacher commands

Here are the building blocks from the `teacher.py` file you can use in your challenges. For example, use `self.fwd()` to drive your robot forward.

* `deg_fwd(angle)` - how many degrees do you want your wheels to rotate? You need to pass the _angle_

* `fwd` - powers on your robot to drive forward. You'll need to use `self.stop()` to power off the motors

* `right` - by default, `self.right()` will give the left motor 90% power and the right 0% which rotates right. You can use kwargs to adjust the power such as `self.right(primary=90, counter=-90)`, which will spin the robot in place

* `left` - same as right but reversed.

* `back` - same as fwd but in reverse.

* `servo` - moves the servo (plugged into servo1) to the given value (use 1000 - 2000)

* `stop` - sets motor power to zero

* `read_distance` - returns the distance from the distance sensor (plugged into I2C port) in milimeters

* `get_heading` - returns the gyroscope's value
