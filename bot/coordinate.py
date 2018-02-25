class Coordinate:
    ERROR_ADD = "Failed to add."

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, displacement=None):
        if displacement and type(displacement) == Coordinate:
            dx, dy = displacement.x, displacement.y
        elif hasattr(displacement, '__len__') and len(displacement) == 2:
            dx, dy = displacement
        else:
            raise Exception(self.ERROR_ADD)
        sumx, sumy = self.x + dx, self.y + dy
        return Coordinate(x=sumx, y=sumy)
