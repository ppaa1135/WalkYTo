import sys
import os

import rospy
from gazebo_msgs.srv import *

class time:
	def __init__(self, secs, nsecs):
		self.secs = secs
		self.nsecs = nsecs

def apply_joint_effort(joint_name, effort, start_time, duration ):
    rospy.wait_for_service('gazebo/apply_joint_effort')
    
    try:
        # create a handle to the add_two_ints service
        apply_joint = rospy.ServiceProxy('gazebo/apply_joint_effort', ApplyJointEffort, persistent=True)
        
        # simplified style
        resp1 = apply_joint(joint_name, effort, start_time, duration)
        # print(resp1.success)
        # print(resp1.status_message)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# if __name__ == "__main__":
# 	joint_name1 = 'MS_Faraday_imu::1'
# 	joint_name2 = 'MS_Faraday_HW_0::1'
# 	effort = 4000
# 	start_time = time(0, 0)
# 	duration = time(1, 0)

#    	apply_joint_effort(joint_name1, effort, start_time, duration)
#    	# apply_joint_effort(joint_name2, effort, start_time, duration)
