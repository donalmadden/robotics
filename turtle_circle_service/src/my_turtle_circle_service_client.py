#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('turtle_circle_service_client')
rospy.wait_for_service('/move_turtle_in_circle')
my_service_client = rospy.ServiceProxy('/move_turtle_in_circle', Empty)
request_object = EmptyRequest()

result = my_service_client(request_object)

print result
