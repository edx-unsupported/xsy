from datetime import datetime
from pytz import timezone

from will.plugin import WillPlugin
from will.decorators import respond_to
import pprint


class TimeConverterPlugin(WillPlugin):

    TIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z%z"

    @respond_to("^what time is it in (?P<location>\w+)")
    def time_now(self, message, location):
        """
        Show the current time in (pakistan/cambridge): It is 7.00 PM in Pakistan.
        """
        if location == "pakistan":
            zone = 'Karachi'
        else:
            zone = 'UTC'

        now_time = datetime.now(timezone(zone))
        time = now_time.strftime(self.TIME_FORMAT)

        self.reply(message, "It is {time} in {location}".format(time=time, location=location))

    @respond_to("^what time is (?P<time>\S+) (?(A|P)M) in (?P<location>\S+)")
    def time_particular(self, message, time, am_pm, location):
        """
        Show the particular time in (pakistan/cambridge): It would be 7.00 PM in Pakistan.
        """
        if location == "pakistan":
            zone = 'Karachi'
        else:
            zone = 'UTC'

        zone_time = datetime.datetime(timezone(zone))
        time = zone_time.strftime(self.TIME_FORMAT)

        self.reply(message, "It is {time} in {location}".format(time=time, location=location))