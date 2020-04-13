#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('move_turtle_service_client')
rospy.wait_for_service('/move_turtle_in_arc')
move_turtle_service_client = rospy.ServiceProxy('/move_turtle_in_arc', Empty)
request_object = EmptyRequest()
result = move_turtle_service_client(request_object)
print result
