
class Alien:
    """
    Class Alien
    """
    total_aliens_created = 0
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1
    def hit(self):
        self.health -= 1
        return self.health
    def is_alive(self):
        return self.health>0
    
    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        return self.x_coordinate, self.y_coordinate
    def collision_detection(self, object):
        pass
def new_aliens_collection(aliens):
    res = [Alien(al[0], al[1]) for al in aliens]
    return res