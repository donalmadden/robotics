#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def callback(msg):
    print("x = " + str(msg.x))
    print("y = " + str(msg.y))
    print("theta = " + str(msg.theta))
    print("lin vel = " + str(msg.linear_velocity))
    print("ang vel = " + str(msg.angular_velocity))

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/turtle1/pose', Pose, callback)
rospy.spin()
