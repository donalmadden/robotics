#!/usr/bin/env python

import rospy
from lab_03_sols.srv import CircleDuration, CircleDurationRequest

rospy.init_node('move_turtle_service_client')
rospy.loginfo("Waiting for service")
rospy.wait_for_service('/move_turtle_in_circle')
rospy.loginfo("Service ready")
turtle_service_client = rospy.ServiceProxy('/move_turtle_in_circle', CircleDuration)
turtle_request_object = CircleDurationRequest()
turtle_request_object.duration = 10
rospy.loginfo("Doing Service Call...")
result = turtle_service_client(turtle_request_object)
rospy.loginfo(str(result)) # Print the result given by the service called
rospy.loginfo("END of Service call...")
