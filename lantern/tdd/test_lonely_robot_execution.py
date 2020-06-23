import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, RobotFallsFromAsteroidError


class TestRobotCreation:

    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x, y)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)

        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size, robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            robot = Robot(*robot_coordinates, asteroid, "W")
            robot.check_robot_miss_asteroid()


class TestRobotMovement:
    x, y = 10, 15
    asteroid = Asteroid(x, y)

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        )
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
                ("N", "E"),
                ("W", "N"),
                ("S", "W"),
                ("E", "S")
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, robot_coordinates, expected_coordinates",
        (
                ("N", (3, 20), (3, 21)),
                ("W", (-1, 6), (-2, 6)),
                ("S", (10, 0), (10, -1)),
                ("E", (10, 2), (11, 2)),
        )
    )
    def test_move_forward(self, current_direction, robot_coordinates, expected_coordinates):
        robot = Robot(*robot_coordinates, self.asteroid, current_direction)
        robot.move_forward()
        assert (robot.x, robot.y) == expected_coordinates

        # check if robot falls from asteroid during movement
        with pytest.raises(RobotFallsFromAsteroidError):
            robot.check_robot_falls_from_asteroid()
            assert robot_coordinates == (robot.x, robot.y)

    @pytest.mark.parametrize(
        "current_direction, robot_coordinates, expected_coordinates",
        (
                ("N", (3, 20), (3, 19)),
                ("W", (10, 2), (11, 2)),
                ("S", (18, 45), (18, 46)),
                ("E", (0, 8), (-1, 8)),
        )
    )
    def test_move_backward(self, current_direction, robot_coordinates, expected_coordinates):
        robot = Robot(*robot_coordinates, self.asteroid, current_direction)
        robot.move_backward()
        assert (robot.x, robot.y) == expected_coordinates

        # check if robot falls from asteroid during movement
        with pytest.raises(RobotFallsFromAsteroidError):
            robot.check_robot_falls_from_asteroid()
            assert robot_coordinates == (robot.x, robot.y)

