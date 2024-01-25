#!/usr/bin/env python

# TODO: import ?????????
# TODO: import ???????_msgs.msg
# TODO: import ??????????_msgs.msg
import rospy
import actionlib
import control_msgs.msg
import trajectory_msgs.msg

# TODO: ACTION_NAME = ???
# TODO: JOINT_NAME = ???
TIME_FROM_START = 5  # How many seconds it should take to set the torso height.
JOINT_NAME = "torso_lift_joint"
ACTION_NAME = "/torso_controller/follow_joint_trajectory"

class Torso(object):
    """Torso controls the robot's torso height.
    """
    MIN_HEIGHT = 0.0
    MAX_HEIGHT = 0.4

    def __init__(self):
        # TODO: Create actionlib client
        global client 
        client = actionlib.SimpleActionClient(ACTION_NAME, control_msgs.msg.FollowJointTrajectoryAction)
        # TODO: Wait for server
        client.wait_for_server()
        pass

    def set_height(self, height):
        """Sets the torso height.

        This will always take ~5 seconds to execute.

        Args:
            height: The height, in meters, to set the torso to. Values range
                from Torso.MIN_HEIGHT (0.0) to Torso.MAX_HEIGHT(0.4).
        """
        # TODO: Check that the height is between MIN_HEIGHT and MAX_HEIGHT.
        if height > self.MAX_HEIGHT:
            height = self.MAX_HEIGHT
        elif height < self.MIN_HEIGHT:
            height = self.MIN_HEIGHT
        else:
            pass
        # TODO: Create a trajectory point
        point = trajectory_msgs.msg.JointTrajectoryPoint()
        # TODO: Set position of trajectory point
        point.positions = [height]
        # TODO: Set time of trajectory point
        point.time_from_start = rospy.Time(TIME_FROM_START)

        # TODO: Create goal
        goal = control_msgs.msg.FollowJointTrajectoryGoal()
        # TODO: Add joint name to list
        goal.trajectory.joint_names = [JOINT_NAME]
        # TODO: Add the trajectory point created above to trajectory
        goal.trajectory.points = [point]
        # TODO: Send goal
        client.send_goal(goal)
        # TODO: Wait for result
        client.wait_for_result()
        rospy.logerr('Not implemented.')
