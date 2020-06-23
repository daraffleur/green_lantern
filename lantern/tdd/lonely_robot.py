class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        self.direction = direction

    def turn_left(self):
        turns_left = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.direction = turns_left[self.direction]

    def turn_right(self):
        turns_right = {"N": "E", "W": "N", "S": "W", "E": "S"}
        self.direction = turns_right[self.direction]

    def move_forward(self):
        dict_move_forward = {
            "N": (self.x, self.y + 1),
            "W": (self.x - 1, self.y),
            "S": (self.x, self.y - 1),
            "E": (self.x + 1, self.y)}
        self.x, self.y = dict_move_forward[self.direction]

    def move_backward(self):
        dict_move_backward = {
            "N": (self.x, self.y - 1),
            "W": (self.x + 1, self.y),
            "S": (self.x, self.y + 1),
            "E": (self.x - 1, self.y)}
        self.x, self.y = dict_move_backward[self.direction]

    def check_robot_miss_asteroid(self):
        # check if robot miss asteroid while landing
        if self.x > self.asteroid.x or self.x < 0 or self.y > self.asteroid.y or self.y < 0:
            raise MissAsteroidError("Robot missed asteroid while landing")

    def check_robot_falls_from_asteroid(self):
        # check if robot falls from asteroid during movement
        if self.asteroid.x < self.x or self.x < 0 or self.asteroid.y < self.y or self.y < 0:
            raise RobotFallsFromAsteroidError("Robot fell down from asteroid")


class MissAsteroidError(Exception):
    pass


class RobotFallsFromAsteroidError(Exception):
    pass

