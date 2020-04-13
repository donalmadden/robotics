#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
rospy.init_node('topic_publisher')
#pub = rospy.Publisher('/counter', Int32, queue_size=1)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

rate = rospy.Rate(2)
_again = Twist()
_again.linear.x = 0.9
_again.linear.y = 0.0
_again.linear.z = 0.0
_again.angular.x = 0.0
_again.angular.y = 0.0
_again.angular.z =  0.5
#count = Int32()
#count.data = 0

while not rospy.is_shutdown():
    pub.publish(_again)
    #count.data +=1
    rate.sleep()
