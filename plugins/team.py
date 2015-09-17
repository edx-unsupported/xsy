from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template
import pprint


class TeamPlugin(WillPlugin):

    @hear("(?P<before>.*)@team(?P<after>.*)")
    def send_to_team(self, message,before,after):
        channel = self.get_room_from_message(message)['name']
        notification_list = self.load("team_" + channel, None)
        if notification_list and message.sender:
            self.say("{} said: {}team{} ({})".format(message.sender.nick, before, after, ' '.join('@'+user for user in notification_list)), room=self.get_room_from_message(message), notify=True)

    @respond_to("^add (@?)(?P<user>\S+) to (this )?team")
    def add_to_team(self, message, user):
        """
        add [user] to this team: request to be notified when someone mentions team
        """
        if user == "me":
            user = message.sender.nick
        channel = self.get_room_from_message(message)['name']
        notification_list = self.load("team_" + channel, None)
        if not notification_list:
            notification_list = []
        notification_list.append(user)
        notification_list = list(set(notification_list))
        self.save('team_' + channel, notification_list)
        self.reply(message, "team for {} is now: {}".format(channel, ', '.join(user for user in notification_list)))

    @respond_to("^set (this )?team to (?P<users>(.*))")
    def set_team(self, message, users):
        """
        set team to user, user, user: bulk update the whole team
        """
        channel = self.get_room_from_message(message)['name']
        notification_list = [u.replace('@', '').replace(',', '') for u in users.split(' ')]
        notification_list = list(set(notification_list))
        self.save('team_' + channel, notification_list)
        self.reply(message, "team for {} is now: {}".format(channel, ', '.join(user for user in notification_list)))

    @respond_to("^remove (@?)(?P<user>\S+) from (this )?team")
    def remove_from_team(self, message, user):
        """
        remove [user] from this team: remove a person from this team
        """
        if user == "me":
            user = message.sender.nick
        channel = self.get_room_from_message(message)['name']
        notification_list = self.load("team_" + channel, None)
        if not notification_list:
            notification_list = []
        notification_list.remove(user)
        notification_list = list(set(notification_list))
        self.save('team_' + channel, notification_list)
        self.reply(message, "team for {} is now: {}".format(channel, ', '.join(user for user in notification_list)))

    @respond_to("^who is on (this )?team")
    def check_team(self, message):
        """
        who is on this team: see who is on the team for this room.
        """
        channel = self.get_room_from_message(message)['name']
        notification_list = self.load("team_" + channel, None)
        if notification_list:
            self.reply(message, "Team for {}:  {}".format(channel, ', '.join(notification_list)))
        else:
            self.reply(message, "There is no one on this team")



