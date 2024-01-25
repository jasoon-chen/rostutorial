#!/usr/bin/env python
import math
import rospy
import actionlib
import control_msgs.msg
import trajectory_msgs.msg

LOOK_AT_ACTION_NAME = "/head_controller/point_head"
PAN_TILT_ACTION_NAME = "/head_controller/follow_joint_trajectory"
PAN_JOINT = "head_pan_joint"
TILT_JOINT = "head_tilt_joint"
PAN_TILT_TIME = 2.5

class Head(object):
    MIN_PAN = math.radians(-90)
    MAX_PAN = math.radians(90)
    MIN_TILT = math.radians(-45)
    MAX_TILT = math.radians(90)
    def __init__(self):
        self.lookClient = actionlib.SimpleActionClient(LOOK_AT_ACTION_NAME, control_msgs.msg.PointHeadAction)
        self.panClient = actionlib.SimpleActionClient(PAN_TILT_ACTION_NAME, control_msgs.msg.FollowJointTrajectoryAction)
        self.lookClient.wait_for_server()
        self.panClient.wait_for_server()
    
    def look_at(self, frame_id, x, y, z):
        goal = control_msgs.msg.PointHeadGoal()
        goal.min_duration = rospy.Time(1)
        
        point = goal.target.point
        point.x,point.y,point.z = x, y, z

        goal.target.header.frame_id = frame_id

        self.lookClient.send_goal(goal)
        self.lookClient.wait_for_result()

        rospy.logerr("Done Pan Tilt")
    
    def pan_tilt( self, pan, tilt ):
        pan = max(self.MIN_PAN, pan)
        pan = min(self.MAX_PAN, pan)

        tilt = max(self.MIN_TILT, tilt)
        tilt = min(self.MIN_TILT, tilt)

        point = trajectory_msgs.msg.JointTrajectoryPoint()
        point.positions = [pan, tilt]
        point.time_from_start = rospy.Time(PAN_TILT_TIME)

        goal = control_msgs.msg.FollowJointTrajectoryGoal()
        goal.trajectory.joint_names = [PAN_JOINT, TILT_JOINT]
        goal.trajectory.points = [point]

        self.panClient.send_goal(goal)
        self.panClient.wait_for_result

        rospy.logerr("Done Pan Tilt")
