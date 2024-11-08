#given a point, x,y, apply these rules, delete previous point(s)
#do I cut dist in half for each iteration?
## first point
#p1_x = x
#p1_y = y - .36 * dist
## second point
#p2_x = x - .5 * dist
#p2_y = y + .5 * dist
## third point
#p3_x = x + .5 * dist
#p3_y = y + .5 * dist

class Point():
  def __init__(self, x, y, dist):
    self.x = x
    self.y = y
    self.dist = dist
    self.color = (20,200,50)

  def draw(self, game):
    game.screen.set_at((self.x, self.y), self.color)

def generate_points(points):
  generated_points = []
  for point in points:
    # first point
    point_1_x = point.x
    point_1_y = point.y - .36 * point.dist
    # second point
    point_2_x = point.x - .5 * point.dist
    point_2_y = point.y + .5 * point.dist
    # third point
    point_3_x = point.x + .5 * point.dist
    point_3_y = point.y + .5 * point.dist

    point_1 = Point(int(point_1_x), int(point_1_y), point.dist / 2)
    point_2 = Point(int(point_2_x), int(point_2_y), point.dist / 2)
    point_3 = Point(int(point_3_x), int(point_3_y), point.dist / 2)
    generated_points.append(point_1)
    generated_points.append(point_2)
    generated_points.append(point_3)

  return generated_points