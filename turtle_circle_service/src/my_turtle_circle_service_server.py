#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyResponse

def my_callback(request):
    print "My turtle circle callback has been called"
    pub = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=1)

    rate = rospy.Rate(2)
    _again = Twist()
    _again.linear.x = 0.9
    _again.linear.y = 0.0
    _again.linear.z = 0.0
    _again.angular.x = 0.0
    _again.angular.y = 0.0
    _again.angular.z =  0.5

    while not rospy.is_shutdown():
        pub.publish(_again)

    return EmptyResponse()

rospy.init_node('turtle_circle_service_server')

my_service = rospy.Service('/move_turtle_in_circle', Empty, my_callback)

rospy.spin()
