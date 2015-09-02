from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template
import pprint


class BirthdayPlugin(WillPlugin):

    @respond_to("^sing happy birthday to (@?)(?P<user>\S+)")
    def singhappybirthday(self, message, user):
        """
        sing happy birthday to [user]: Sing happy birthday to a user
        """
        if user == "me":
            user = message.sender.nick
        self.say("Happy birthday to you!\nHappy birthday to you!\nHappy birthday, dear {}\nHappy birthday to you!\n(cake)".format(user), room=self.get_room_from_message(message))


