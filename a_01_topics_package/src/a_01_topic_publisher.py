#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('a_01_topic_publisher')
pub = rospy.Publisher('/a_01_counter', Int32, queue_size=1)

rate = rospy.Rate(2)
count = Int32()
count_data = 0

while not rospy.is_shutdown():
    pub.publish(count)
    count.data += 1
    rate.sleep()

