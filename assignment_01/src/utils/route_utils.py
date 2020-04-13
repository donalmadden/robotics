import math
from geometry_msgs.msg import Vector3


class RouteUtils(object):

    _origin = None

    def __init__(self):
        self._origin = Vector3()
        self._origin.x = 5.544445
        self._origin.y = 5.544445
        self._origin.z = 0

    def get_origin(self):
        return self._origin

    @classmethod
    def get_distance_to_point(cls, x_, x_goal_, y_, y_goal_):
        return abs(math.sqrt(((x_goal_ - x_) ** 2) + ((y_goal_ - y_) ** 2)))

    @classmethod
    def get_desired_angle(cls, x_, x_goal_, y_, y_goal_):
        return math.atan2(y_goal_ - y_, x_goal_ - x_)

    def build_traversal_order(self, starting_point_, points_to_traverse_, names_to_traverse_, ordered_traversal_list_, ordered_traversal_list_names_):
        _points_to_return = ordered_traversal_list_
        _names_to_return = ordered_traversal_list_names_
        if len(points_to_traverse_) is 0:
            return _points_to_return, _names_to_return
        else:
            _closest_point_distance = 100.0
            _closest_point_index = -1
            for _i in range(len(points_to_traverse_)):
                _distance_to_next_point_in_list = self.get_distance_to_point(starting_point_.x, points_to_traverse_[_i].x, starting_point_.y, points_to_traverse_[_i].y)
                if _distance_to_next_point_in_list < _closest_point_distance:
                    _closest_point_distance = _distance_to_next_point_in_list
                    _closest_point_index = _i
            _next_point = points_to_traverse_.pop(_closest_point_index)
            ordered_traversal_list_names_.append(names_to_traverse_.pop(_closest_point_index))
            ordered_traversal_list_.append(_next_point)
            return self.build_traversal_order(_next_point, points_to_traverse_, names_to_traverse_)
