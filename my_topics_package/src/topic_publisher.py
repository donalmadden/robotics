#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import random 
import math

rospy.init_node('topic_publisher')
#pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)
#move_turtle = Twist()
#move_turtle.linear.x = 0.5
#move_turtle.angular.z = 0.5
spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
#print('test '+str(round(random.uniform(1,2),1)))
#spawn_turtle(round(random.uniform(0.5,10.5),1), 10.5, 0, "turtle2")

# SPAWN N TURTLES
# -------------------------------#
_turtle_coordinates = []
#for _i in range(10):
#    _turtle_coordinates.append((round(random.uniform(0.5,10.5),1), round(random.uniform(5.5,10.5),1)))
#
#for _t in _turtle_coordinates:
#    spawn_turtle(_t[0], _t[1], 0, "turtle"+str(int(_t[0]*_t[1])))
#--------------------------------#

#_turtle_coordinates.append((round(random.uniform(0.5,10.5),1), round(random.uniform(5.5,10.5),1)))
#spawn_turtle(_turtle_coordinates[0][0], _turtle_coordinates[0][1], 0, 'turtle2')

# TURTLE AT TOP
spawn_turtle(6.0,10.2,0, "turtle4")
# TURTLE AT BOTTOM
spawn_turtle(6.0,1.2,0, "turtle5")
#spawn_turtle(0.5,5.5,0, "turtle5")
#spawn_turtle(10.5,5.5,0, "turtle6")


while not rospy.is_shutdown():
#    pub.publish(move_turtle)
    rate.sleep()
