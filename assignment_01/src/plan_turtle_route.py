#!/usr/bin/env python
import rospy
from assignment_01.srv import OrderedTurtles, OrderedTurtlesResponse
from utils import route_utils


def build_traversal_order(starting_point_, points_to_traverse_, names_to_traverse_, ordered_traversal_list_=[],
                          ordered_traversal_list_names_=[]):
    _turtles = ordered_traversal_list_
    _names = ordered_traversal_list_names_
    if len(points_to_traverse_) is 0:
        return _turtles, _names
    else:
        _closest_point_distance = 100.0
        _closest_point_index = -1
        for _i in range(len(points_to_traverse_)):
            _distance_to_next_point_in_list = route_utils.RouteUtils.get_distance_to_point(starting_point_.x,
                                                                                           points_to_traverse_[_i].x,
                                                                                           starting_point_.y,
                                                                                           points_to_traverse_[_i].y)
            if _distance_to_next_point_in_list < _closest_point_distance:
                _closest_point_distance = _distance_to_next_point_in_list
                _closest_point_index = _i
        _next_point = points_to_traverse_.pop(_closest_point_index)
        ordered_traversal_list_names_.append(names_to_traverse_.pop(_closest_point_index))
        ordered_traversal_list_.append(_next_point)
        return build_traversal_order(_next_point, points_to_traverse_, names_to_traverse_, ordered_traversal_list_,
                                     ordered_traversal_list_names_)


def my_callback(request):
    rospy.loginfo("Service /plan_turtle_route service server has been called")
    _origin = utils.get_origin()

    resp = OrderedTurtlesResponse()
    resp.orderedCoordinates, resp.orderedNames = build_traversal_order(_origin, request.coordinates, request.names)

    rospy.loginfo("Finished service /plan_turtle_route")

    return resp


utils = route_utils.RouteUtils()
rospy.init_node('plan_turtle_route')
rate = rospy.Rate(1)
_ = rospy.Service('/plan_turtle_route', OrderedTurtles, my_callback)
while not rospy.is_shutdown():
    rate.sleep()
