import emoji
from flask import Flask
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
        if unicode_val in emoji.UNICODE_EMOJI_ALIAS.keys():
            infodict['emojicodeAlias'] = emoji.UNICODE_EMOJI_ALIAS[unicode_val]
        return infodict

class EmojicodeResouce(Resource):
    def get(self, emojicode):
        infodict = { 
            'emojiUnicode': None,
            'emojicode': emojicode,
            'emojicodeAlias': None 
        }
        if emojicode in emoji.EMOJI_UNICODE.keys():
            infodict['emojiUnicode'] = emoji.EMOJI_UNICODE[emojicode]
        if infodict['emojiUnicode'] is not None:
            infodict['emojicodeAlias'] = emoji.UNICODE_EMOJI_ALIAS[infodict['emojiUnicode']]
        return infodict

class EmojicodeAliasResouce(Resource):
    def get(self, alias):
        infodict = { 
            'emojiUnicode': None,
            'emojicode': None,
            'emojicodeAlias': alias 
        }
        if alias in emoji.EMOJI_ALIAS_UNICODE.keys():
            infodict['emojiUnicode'] = emoji.EMOJI_ALIAS_UNICODE[alias]
        if infodict['emojiUnicode'] is not None:
            infodict['emojicode'] = emoji.UNICODE_EMOJI[infodict['emojiUnicode']]
        return infodict

api.add_resource(UnicodeResource, '/unicode/<string:unicode_val>')
api.add_resource(EmojicodeResouce, '/emojicode/<string:emojicode>')
api.add_resource(EmojicodeAliasResouce, '/alias/<string:alias>')

if __name__ == '__main__':
    app.run(debug=False)
