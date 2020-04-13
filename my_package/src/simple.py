#!/usr/bin/env python

import rospy

rospy.init_node('Rodney')
rate = rospy.Rate(2)
while not rospy.is_shutdown():
	print "We don't serve fine wine in half-pints, buddy"
	rate.sleep()
