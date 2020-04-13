#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('service_client')
rospy.wait_for_service('/my_service')
my_service_client = rospy.ServiceProxy('/my_service', Empty)
request_object = EmptyRequest()

result = my_service_client(request_object)

print result
