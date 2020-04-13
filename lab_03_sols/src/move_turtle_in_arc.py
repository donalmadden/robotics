#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

def my_callback(request):
   rospy.loginfo("Service /move_turtle_in_arc has been called")
   move_turtle.linear.x = 0.5
   move_turtle.angular.z = 0.5
   pub.publish(move_turtle)
   rospy.loginfo("Finished service /move_turtle_in_arc")
   return EmptyResponse()

rospy.init_node('move_turtle_service_server')
move_turtle_service = rospy.Service('/move_turtle_in_arc', Empty, my_callback)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
move_turtle = Twist()
rospy.spin() # keep the service open
