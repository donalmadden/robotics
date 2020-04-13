#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Kill
PI = 3.1415926535897

def rotate():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Receiveing the user's input
    print("Let's rotate your robot")
    #speed = input("Input your speed (degrees/sec):")
    speed = 30
    angle = input("Type your distance (degrees):")
    distance = input("Type your distance :")
    #clockwise = input("Clockwise?: ") #True or false
    clockwise = False
    if angle < 0:
        print('in if')
        clockwise = True
    #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360
    print(relative_angle)
    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Checking if our movement is CW or CCW
    if clockwise:
        print('in 2nd if')
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < abs(relative_angle)):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
        print(current_angle)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
   # rospy.spin()

    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    vel_msg.linear.x = abs(speed)
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)
    kill_turtle = rospy.ServiceProxy('kill', Kill)
    kill_turtle('turtle5')
    #kill_publisher = rospy.Publisher('/kill', Kill, queue_size=1)
    #kill_msg = Kill()
    #kill_msg.name = 'turtle5'
    #kill_publisher.publish(kill_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass
