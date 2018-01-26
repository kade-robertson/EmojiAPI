# EmojiAPI :exclamation:

An utterly useless Emoji API, built on REST principles. :boom:

A demo is available at https://emojis.trade/ for your convenience.

### Why? :question:

A better question -- why not? All of those per-language libraries are such a pain to use in the first place. Why not have a service which can be used the same way in any language? :heart_eyes:

### Usage :information_source:

- `/unicode/:emoji`: Provide a Unicode emoji, and the appropriate emoji code and alias will be returned, if available.
- `/emojicode/:code`: Provide a valid emoji code, and the appropriate Unicode emoji and alias will be returned, if available.
- `/alias/:alias`: provide a valid emoji code alias, and the appropriate Unicode emoji and emoji code will be returned, if available.

All response bodies have the same structure:
```json
{
    emojiUnicode: "😏",
    emojiCode: ":smirking_face:",
    emojiCodeAlias: ":smirk:"
}
```

Any of these values can also be `null` if no corresponding data exists.

### Examples :speech_balloon:

[`https://emojis.trade/unicode/💩`](https://emojis.trade/unicode/💩) returns

```json
{
    emojiCode: ":pile_of_poo:",
    emojiCodeAlias: ":poop:",
    emojiUnicode: "💩"
}
```

[`https://emojis.trade/emojicode/:water_wave:`](https://emojis.trade/emojicode/:water_wave:) returns

```json
{
    emojiCode: ":water_wave:",
    emojiCodeAlias: ":ocean:",
    emojiUnicode: "🌊"
}
```

[`https://emojis.trade/alias/:thumbsup:`](https://emojis.trade/alias/:thumbsup:) returns

```json
{
    emojiCode: ":thumbs_up:",
    emojiCodeAlias: ":thumbsup:",
    emojiUnicode: "👍"
}
```
[`https://emojis.trade/emojicode/:notreal:`](https://emojis.trade/emojicode/:notreal:) returns

```json
{
    emojiCode: ":notreal:",
    emojiCodeAlias: null,
    emojiUnicode: null
}
```

### Setting this up :information_source:

1. Clone this repository.
2. Install the requirements with `pip install -r requirements.txt`
3. Optionally turn on debug more, or change the port in the `api.py` file.
4. `python3 api.py` :snake:

### Footnote

*This is not meant to be taken seriously, this was just my first project doing anything web-development-ish in Python.*
