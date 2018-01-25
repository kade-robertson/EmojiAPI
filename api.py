import emoji
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class UnicodeResource(Resource):
    def get(self, unicode_val):
        infodict = { 
            'emojiUnicode': unicode_val,
            'emojicode': None,
            'emojicodeAlias': None 
        }
        if unicode_val in emoji.UNICODE_EMOJI.keys():
            infodict['emojicode'] = emoji.UNICODE_EMOJI[unicode_val]
        else:
            return dict(), 400
        if unicode_val in emoji.UNICODE_EMOJI_ALIAS.keys():
            infodict['emojicodeAlias'] = emoji.UNICODE_EMOJI_ALIAS[unicode_val]
        return infodict, 200

class EmojicodeResouce(Resource):
    def get(self, emojicode):
        infodict = { 
            'emojiUnicode': None,
            'emojicode': emojicode,
            'emojicodeAlias': None 
        }
        if emojicode in emoji.EMOJI_UNICODE.keys():
            infodict['emojiUnicode'] = emoji.EMOJI_UNICODE[emojicode]
        else:
            return dict(), 400
        unicode_val = infodict['emojiUnicode']
        if unicode_val in emoji.UNICODE_EMOJI_ALIAS.keys():
            infodict['emojicodeAlias'] = emoji.UNICODE_EMOJI_ALIAS[unicode_val]
        return infodict

api.add_resource(UnicodeResource, '/unicode/<string:unicode_val>')
api.add_resource(EmojicodeResouce, '/emojicode/<string:emojicode>')

if __name__ == '__main__':
    app.run(debug=True)
