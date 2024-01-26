#!/usr/bin/env python

import rospy
import actionlib
import control_msgs.msg
import sensor_msgs.msg
import robot_api

class JointStateReader(object):
    joint_dict = {}

    def __init__(self):
        rospy.Subscriber("/joint_states", sensor_msgs.msg.JointState, self.callback)
    
    def callback(self, data):
        for i, joint_name in enumerate(data.name):
            self.joint_dict[joint_name] = data.position[i]

    def get_joint(self, name):
        return self.joint_dict.get(name,None)
    
    def get_joints(self, names):
        returnValue = ["","","","","","","","",""]
        for i in range(0, len(names), 1):
            rospy.logerr(i)
            returnValue[i] = self.get_joint(names[i])
        return returnValue