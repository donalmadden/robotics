#!/usr/bin/env python

import rospy
from lab_03_sols.srv import CircleDuration, CircleDurationResponse 
from turtle_move_circle_class import MoveTurtle

def my_callback(request):
    rospy.loginfo("Service has been called")
    moveturtle_object = MoveTurtle()
    moveturtle_object.move_turtle(request.duration)
    rospy.loginfo("Finished service")
    response = CircleDurationResponse()
    response.success = True
    return response

rospy.init_node('move_turtle_service_server_adv')
move_turtle_service = rospy.Service('/move_turtle_in_circle', CircleDuration , my_callback)
rospy.loginfo("Service ready")
rospy.spin() # mantain the service open
