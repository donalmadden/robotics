#!/usr/bin/env python

import rospy
from assignment_01.srv import SpawnTurtles, SpawnTurtlesRequest, OrderedTurtles, OrderedTurtlesRequest
from utils import route_utils

utils = route_utils.RouteUtils()
rospy.init_node('init_factory_floor_service_client')
rospy.wait_for_service('/init_factory_floor')

_origin = utils.get_origin()

move_turtle_service_client = rospy.ServiceProxy('/init_factory_floor', SpawnTurtles)

request_object = SpawnTurtlesRequest()
request_object.numTurtles = 10
result = move_turtle_service_client(request_object)

_turtles_to_clean = result.coordinates

ordered_turtles_request_object = OrderedTurtlesRequest()
ordered_turtles_request_object.coordinates = result.coordinates
ordered_turtles_request_object.names = result.names
plan_turtle_route_service_client = rospy.ServiceProxy('/plan_turtle_route', OrderedTurtles)
result = plan_turtle_route_service_client(ordered_turtles_request_object)
print(result)
