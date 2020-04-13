#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MoveTurtle():

    def __init__(self):
        self.turtle_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1) # 1hz
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
    # Publishing in topics sometimes fails the first time you publish. Account for this here.
        while not self.ctrl_c:
            connections = self.turtle_publisher.get_num_connections()
            if connections > 0:
                self.turtle_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        # works better than rospy.is_shutdown()
        self.stop_turtle()
        self.ctrl_c = True

    def stop_turtle(self):
        self.cmd.linear.x = 0
        self.cmd.angular.z = 0 
        rospy.loginfo("Stopping Turtle!")
        self.publish_once_in_cmd_vel()

    def move_turtle(self, duration, linear_speed=0.5, angular_speed=0.5):
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed
        rospy.loginfo("Moving Turtle!")
        i = 0
        while not self.ctrl_c and i < duration:
            self.publish_once_in_cmd_vel()
            self.rate.sleep()
            i += 1
        self.stop_turtle()

    if __name__ == '__main__':
        rospy.init_node('move_turtle_test', anonymous=True)
        moveturtle_object = MoveTurtle()
        try:
            moveturtle_object.move_turtle(10)
        except rospy.ROSInterruptException:
            pass

