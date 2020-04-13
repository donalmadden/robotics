#!/usr/bin/env python

import rospy

rospy.init_node('Trigger') #Initiate a node called Trigger
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    print("And that's what I've done. Maintained it for 20 years. This old brooms had 17 new heads and 14 new handles in its time.")
    rate.sleep()
