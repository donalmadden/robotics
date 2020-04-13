#!/usr/bin/env python
import rospy
import actionlib
import random
from turtle_actionlib.msg import ShapeAction, ShapeGoal
from std_srvs.srv import Empty, EmptyRequest

# create constants for action state values
PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

def feedback_callback(feedback):
    rospy.loginfo('Feedback message received') # This will never be executed as Shape.action has an empty feedback section

# initialise the action client node
rospy.init_node('turtle_shape_client_node')

# create a client connected to the action server
client = actionlib.SimpleActionClient('/turtle_shape', ShapeAction)

# wait until the action server is up and running
rospy.loginfo('Waiting for Action Server')
client.wait_for_server()
rospy.loginfo('Action Server Found...')

# Wait for the clear service to be running
rospy.wait_for_service('/clear')
# Create the connection to the service
clear_client = rospy.ServiceProxy('/clear', Empty)
# Create an object of type EmptyRequest
request_object = EmptyRequest()

# create a goal to send to the action server and set the attribute values
goal = ShapeGoal()
goal.edges = 3
goal.radius = 2.0

# send the goal to the action server
client.send_goal(goal, feedback_cb=feedback_callback)

# --------------------------------------------------- #
state_result = client.get_state()
rate = rospy.Rate(1)
rospy.loginfo("state_result: "+str(state_result))
#while state_result < DONE:
#   rospy.set_param('/background_b',random.randint(0,255))
#   rospy.set_param('/background_r',random.randint(0,255))
#   rospy.set_param('/background_g',random.randint(0,255))
#   clear_client(request_object)
#   rate.sleep()
#   state_result = client.get_state()
#   rospy.loginfo("state_result: "+str(state_result))

counter = 0
while state_result < DONE:
    rospy.loginfo("Doing stuff while waiting for the server to give a result....")
    counter += 1
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo("state_result: " + str(state_result))
    if counter == 3:
        rospy.logwarn("Canceling goal...")
        client.cancel_goal()
        rospy.logwarn("Goal canceled")
        state_result = client.get_state()
        rospy.loginfo("state_result after cancel : " + str(state_result) + ", counter =" + str(counter))

rospy.loginfo("[Result] State: "+str(state_result))
if state_result == ERROR:
   rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
   rospy.logwarn("There is a warning in the Server Side")
# --------------------------------------------------- #


# wait for the result
#client.wait_for_result()
#rospy.loginfo('Finished!')

