#! /usr/bin/env python

import rospy
#from std_msgs.msg import Int32
from geometry_msgs.msg import Pose

def callback(pose):
    print 'X position: '+str(pose.position.x)
    print 'Y position: '+str(pose.position.y)
    print 'Z position: '+str(pose.position.z)

rospy.init_node('topic_subscriber')

sub = rospy.Subscriber('/counter', Pose, callback)

rospy.spin()

