from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
from will.mixins.room import Room
from datetime import datetime, timedelta
import random


class MakeItSoPlugin(WillPlugin):

    remember_last = timedelta(seconds=300)  # Five minutes

    @hear(r'make it so')
    def makeitso(self, message):
        picards = [
            u'https://thabto.files.wordpress.com/2013/10/make-it-so-captain.jpg',
            u'http://fullnomad.com/wp-content/uploads/2015/08/make-it-so.png',
            u'http://www.andion.co/wp-content/uploads/2013/06/star-trek-make-it-so-450x270.jpg',
            u'http://craftymanolo.com/wordpress/wp-content/uploads/2011/11/make-it-so_2.jpg',
            u'http://media.giphy.com/media/VLoN2iW8ii3wA/giphy.gif',
            u'http://memecrunch.com/meme/11C86/make-it-so/image.png?w=400&c=1',
            u'https://camo.githubusercontent.com/3733c96c13eb749cd2c1d360f85b74678bafab50/687474703a2f2f6d656469612e74756d626c722e636f6d2f33373537393039336235376537363965663161336535386332393936303061642f74756d626c725f696e6c696e655f6e3465646a714967614331717a707137652e676966',
            u'http://lowetide.ca/wp-content/uploads/2011/11/picard-580x360.png',
            u'http://cdn.meme.am/instances/500x/55340824.jpg',
            u'https://qandampa.files.wordpress.com/2013/08/make-it-so.png',
            u'http://i.imgur.com/0eQZ7rN.jpg',
        ]
        beer = u'http://i.imgur.com/YYrVe6s.jpg'
        snow = u'http://i.ytimg.com/vi/KeaehxEdpgo/hqdefault.jpg'

        # Wrap the room in an extra instance of Room(), to work around an issue with
        # getting rooms through v1 of the API. (See https://github.com/skoczen/will/pull/193
        # for resolution of this issue upstream).
        room = Room(**self.get_room_from_message(message))
        if 'id' not in room:
            # v1 API calls the id "room_id", but room.history depends on room['id']
            # This may also get resolved with https://github.com/skoczen/will/pull/193
            room['id'] = room['room_id']
        if room.history[0][u'date'] < room.history[-1][u'date']:
            history = reversed(room.history)
        else:
            history = room.history
        for msg in history:
            if datetime.utcnow() - msg[u'date'] < self.remember_last:
                if 'beer' in msg[u'message']:
                    saying = beer
                    break
                elif 'snow' in msg[u'message']:
                    saying = snow
                    break
        else:  # for-else
            saying = random.choice(picards)
        self.say(saying, room=room)

        picard_count = self.load("picards", 0)
        picard_count += 1
        self.save('picards', picard_count)

    @respond_to("^how many picards")
    def howmanypicards(self, message):
        picard_count = self.load("picards", 0)
        self.reply(message, "There have been {} picards".format(picard_count))
