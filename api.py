import emoji
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class UnicodeResource(Resource):
    def get(self, unicode_val):
        infodict = { 
            'emoji_unicode': unicode_val,
            'emojicode': None,
            'emojicode_alias': None 
        }
        if unicode_val in emoji.UNICODE_EMOJI.keys():
            infodict['emojicode'] = emoji.UNICODE_EMOJI[unicode_val]
        else:
            return dict(), 400
        if unicode_val in emoji.UNICODE_EMOJI_ALIAS.keys():
            infodict['emojicode_alias'] = emoji.UNICODE_EMOJI_ALIAS[unicode_val]
        return infodict, 200

api.add_resource(UnicodeResource, '/unicode/<string:unicode_val>')

if __name__ == '__main__':
    app.run(debug=True)
