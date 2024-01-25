#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Constants
class Base(object):
    """Base controls the mobile base portion of the Fetch robot.

    Sample usage:
        base = robot_api.Base()
        while CONDITION:
            base.move(0.2, 0)
        base.stop()
    """
    _publisher: rospy.Publisher

    def __init__(self):
        # TODO: Create publisher
        self._publisher = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        # rospy.init_node("base", anonymous=True)
        pass
        

    def move(self, linear_speed, angular_speed):
        """Moves the base instantaneously at given linear and angular speeds.

        "Instantaneously" means that this method must be called continuously in
        a loop for the robot to move.

        Args:
            linear_speed: The forward/backward speed, in meters/second. A
                positive value means the robot should move forward.
            angular_speed: The rotation speed, in radians/second. A positive
                value means the robot should rotate clockwise.
        """
        # TODO: Create Twist msg
        msg = Twist()
        # TODO: Fill out msg
        msg.linear.x = linear_speed
        msg.angular.z = angular_speed
        # TODO: Publish msg
        self._publisher.publish(msg)
        # rospy.logerr('Not implemented.')

    def stop(self):
        """Stops the mobile base from moving.
        """
        # TODO: Publish 0 velocity
        msg = Twist()
        msg.linear.x = 0
        msg.angular.z = 0
        self._publisher.publish(msg)
        # rospy.logerr('Not implemented.')
