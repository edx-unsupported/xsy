from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template
import pprint


class HousePointsPlugin(WillPlugin):

  @hear("(?P<points>\d*) points (?P<operator>(to|from)) (?P<housename>.*)")
  def give_points(self, message, points, operator, housename):
        """
        [number] points to|from [house]: grant points to a house
        """
        if housename == "me":
            housename = message.sender.nick
        housepoints = self.load("housepoints", None)
        if not housepoints:
            housepoints = {}
            housepoints[housename] = 0
        if operator == "to":
            housepoints[housename] = housepoints[housename] + int(points)
        else:
            housepoints[housename] = housepoints[housename] - int(points)
        self.save('housepoints', housepoints)
        self.reply(message, "{} now has {} points!".format(housename, housepoints[housename]))

  @respond_to("^what are the house points?")
  def check_points(self, message):
        """
        what are the house points?: see the house points
        """
        housepoints = self.load("housepoints" , None)
        if housepoints:
            self.reply(message, "The House points are:{}".format(housepoints))

