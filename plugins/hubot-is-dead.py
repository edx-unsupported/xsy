from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import random


class HubotDeadPlugin(WillPlugin):

    @hear("^@?hubot")
    def hubotisdead(self, message):
        self.reply(message,"hubot is dead, but I might be able to help. say \"@xsy help\" to see what I can do!") 


    
