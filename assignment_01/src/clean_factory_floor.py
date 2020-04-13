#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse
from assignment_01.srv import OrderedTurtles, OrderedTurtlesResponse
from turtlesim.srv import Spawn
from geometry_msgs.msg import Vector3
import random


def my_callback(request):
    # rospy.loginfo("Service /clean_factory_floor has been called " + str(request.numTurtles))
    rospy.loginfo("Service /clean_factory_floor has been called {}".format(request.names))
    # print("Service /clean_factory_floor has been called {}".format(request.names))

    # # SPAWN N TURTLES
    # # -------------------------------#
    # _turtle_coordinates = []
    # _created_turtle_locations = []
    # _created_turtle_names = []
    # for _i in range(int(request.numTurtles)):
    #     _turtle_coordinates.append((round(random.uniform(0.5, 10.5), 3), round(random.uniform(5.5, 10.5), 3)))
    #
    # for _idx, _t in enumerate(_turtle_coordinates, 2):
    #     _name = "turtle" + str(_idx)
    #     spawn_turtle(_t[0], _t[1], 0, "turtle" + str(_idx))
    #     _turtle_loc = Vector3()
    #     _turtle_loc.x = _t[0]
    #     _turtle_loc.y = _t[1]
    #     _turtle_loc.z = 0
    #     _created_turtle_locations.append(_turtle_loc)
    #     _created_turtle_names.append(_name)
    # # --------------------------------#
    #
    rospy.loginfo("Finished service /clean_factory_floor")
    resp = OrderedTurtlesResponse()
    resp.success = True
    # resp.names = _created_turtle_names
    return resp


rospy.init_node('init_clean_factory_floor_service_server')
rate = rospy.Rate(1)
# spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
_ = rospy.Service('/clean_factory_floor', OrderedTurtles, my_callback)
# pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
# move_turtle = Twist()
while not rospy.is_shutdown():
#    pub.publish(move_turtle)
    rate.sleep()
# rospy.spin()  # keep the service open
