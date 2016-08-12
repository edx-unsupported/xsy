from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import random


class ShipitPlugin(WillPlugin):

    @hear("ship(ping|z|s|ped)?\s*it")
    def shipit(self, message):
        squirrels = [
                  "http://28.media.tumblr.com/tumblr_lybw63nzPp1r5bvcto1_500.jpg",
                  "http://i.imgur.com/DPVM1.png",
                  "http://d2f8dzk2mhcqts.cloudfront.net/0772_PEW_Roundup/09_Squirrel.jpg",
                  "http://www.cybersalt.org/images/funnypictures/s/supersquirrel.jpg",
                  "http://www.zmescience.com/wp-content/uploads/2010/09/squirrel.jpg",
                  "https://dl.dropboxusercontent.com/u/602885/github/sniper-squirrel.jpg",
                  "http://1.bp.blogspot.com/_v0neUj-VDa4/TFBEbqFQcII/AAAAAAAAFBU/E8kPNmF1h1E/s640/squirrelbacca-thumb.jpg",
                  "https://dl.dropboxusercontent.com/u/602885/github/soldier-squirrel.jpg",
                  "https://dl.dropboxusercontent.com/u/602885/github/squirrelmobster.jpeg",
                ]
        self.say(random.choice(squirrels), room=self.get_room_from_message(message)) 
        squirrel_count = self.load("squirrels", 0)
        squirrel_count += 1
        self.save('squirrels', squirrel_count)


    @respond_to("^how many squirrels")
    def howmanysquirrels(self, message):
        squirrel_count = self.load("squirrels", 0)
        self.reply(message, "squirrels = " + str(squirrel_count))
    
    
