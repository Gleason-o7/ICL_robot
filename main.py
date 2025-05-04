from random import randrange
class Robot():
    _active_ids = set()

    def __init__(self, name=None):
        self._id = self._get_unique_id()
        self.name = name

    @classmethod
    def _get_unique_id(cls):
        while True:
            new_id = randrange(100)
            if new_id not in cls._active_ids:
                cls._active_ids.add(new_id)
                return new_id
            
    @property
    def id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"Robot:\n{{\n\tName: {self.name},\n\tID: {self.id}\n}}"
        
robot1 = Robot()

print(robot1)

robot2 = Robot("r")
print(robot2)

robot3 = Robot("a")
print(robot3)