from random import randrange

# Constants
ID_RANGE = 100 # Range of possible Ids
LOWER_BOUND = 0 # Lower bound of 2d array
UPPER_BOUND = 9 # Upper bound of 2d array
MIDPOINT = (UPPER_BOUND - LOWER_BOUND + 1) // 2

class Robot():
    # Class-level sets to track active robot IDs and occupied coordinates
    _active_ids = set()
    _occupied_coordinates = set()

    def __init__(self, name=None, coordinates=None, direction=None):
        self._id = self._get_unique_id()
        self.name = name
        self._coordinates = None
        self._direction = direction
        # Try to set coordinates only if given
        if coordinates is not None:
            # if set_coordinates succeeds, it assigns the coords and returns true
            if not self.set_coordinates(coordinates):
                print(f"Robot {self.name or self._id} could not be placed at {coordinates}.")

    @classmethod
    def get_occupied_coordinates(cls):
        return cls._occupied_coordinates.copy()

    @classmethod
    def _get_unique_id(cls):
        while True:
            new_id = randrange(ID_RANGE)
            if new_id not in cls._active_ids:
                cls._active_ids.add(new_id)
                return new_id


    @staticmethod
    def _within_bounds(coordinates):
        x, y = coordinates
        return LOWER_BOUND <= x <= UPPER_BOUND and LOWER_BOUND <= y <= UPPER_BOUND
    
    @property
    def id(self):
        return self._id
    
    def set_direction(self, direction):
        if direction in ("n", "s", "e", "w"):
            self._direction = direction
            return True
        else:
            print("Invalid direction, options: [n|s|e|w]")
            return False
    
    @property
    def quadrant(self):
        if self._coordinates is None:
            return "Unplaced"
        
        x, y = self._coordinates
        if x > MIDPOINT and y > MIDPOINT:
            return "I"
        elif x < MIDPOINT and y > MIDPOINT:
            return "II"
        elif x < MIDPOINT and y < MIDPOINT:
            return "III"
        elif x > MIDPOINT and y < MIDPOINT:
            return "IV"
        else:
            return "inter-planar"


    @property
    def coordinates(self):
        return self._coordinates
    
    def set_name(self, name):
        self.name = name
    
    def can_move(self, coordinates):
        # Index out-of-bounds check
        if not self._within_bounds(coordinates):
            print(f"Coordinates {coordinates} are out of bounds (must be between ({LOWER_BOUND},{LOWER_BOUND}) and ({UPPER_BOUND},{UPPER_BOUND})).")
            return False

        # Index already taken check
        if coordinates in Robot._occupied_coordinates:
            print(f"Invalid move: Coordinates {coordinates} already occupied.")
            return False
        return True

    def set_coordinates(self, coordinates):
        if not self.can_move(coordinates):
            return False

        # Free previous index
        if self._coordinates:
            Robot._occupied_coordinates.remove(self._coordinates)
        
        # Finally, set new coordinates
        self._coordinates = coordinates
        Robot._occupied_coordinates.add(self._coordinates)
        return True
    
    def move_forward(self):
        if self._coordinates is None:
            print("Cannot move: robot is unplaced.")
            return False

        x, y = self._coordinates


        if self._direction == "n":
            dx, dy = -1, 0
        elif self._direction == "s":
            dx, dy = 1, 0
        elif self._direction == "e":
            dx, dy, = 0, 1
        elif self._direction == "w":
            dx, dy = 0, -1
        else: 
            return False
        
        new_coordinates = (x + dx, y + dy)
        return self.set_coordinates(new_coordinates)

    def __str__(self):
        return (
            f"Robot:\n{{\n"
            f"\tName: {self.name},\n"
            f"\tID: {self._id},\n"
            f"\tLocation: {self._coordinates},\n"
            f"\tQuadrant: {self.quadrant}\n}}"
        )
    

# AI-generated test cases
# === Example usage ===

# Create robots and attempt to place them
robot1 = Robot("Alpha", (2, 3))
print(robot1)

robot2 = Robot("Beta", (2, 4))  # Will fail - spot taken
print(robot2)
robot2.set_direction("w")
robot2.move_forward()
print(robot2)
#robot3 = Robot("Gamma", (9, 9))
#print(robot3)

# robot4 = Robot("Delta", (10, 10))  # Will fail - out of bounds
# print(robot4)

# Attempt to move robot3 to an occupied space
#robot3.set_coordinates((2, 3))

# Move robot3 to a free, valid space
# robot3.set_coordinates((5, 5))
# print(robot3)

# Show occupied coordinates
print("Occupied coordinates:", Robot.get_occupied_coordinates())
