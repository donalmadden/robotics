#!/usr/bin/env python

import rospy
from lab_03_sols.srv import CircleDuration, CircleDurationResponse
from geometry_msgs.msg import Twist

def my_callback(request):
   rospy.loginfo("Service has been called")
   move_turtle.linear.x = 0.5
   move_turtle.angular.z = 0.5
   i = 0
   while i < request.duration:
      pub.publish(move_turtle)
      rate.sleep()
      i += 1
   move_turtle.linear.x = 0
   move_turtle.angular.z = 0
   pub.publish(move_turtle)
   rospy.loginfo("Finished service")
   response = CircleDurationResponse()
   response.success = True
   return response

rospy.init_node('move_turtle_service_server') 
move_turtle_service = rospy.Service('/move_turtle_in_circle', CircleDuration, my_callback)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
move_turtle = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service ready")
rospy.spin() # maintain the service open.
