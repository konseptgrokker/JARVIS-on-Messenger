import modules
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities=None):
    help = 'Hi there! I\'m Jarvis, your personal assistant.'
    if entities is not None:
        if 'sender' in entities and 'first_name' in entities['sender']:
            sender_name = entities['sender']['first_name']
            help = help.replace('there', sender_name)
    help += (
        '\n\nYou can tell me things like:'
        '\n  - define comfort'
        '\n  - iron man 2 movie plot'
        '\n  - tell me a joke/quote/fact'
        '\n  - wiki html'
        '\n  - anything you want book'
        '\n  - usd to eur rate'
        '\n  - death note anime'
        '\n  - time in seattle'
        '\n  - songs by linkin park'
        '\n  - shorten google.com'
        '\n  - weather in london'
        '\n  - videos of sia'
        '\n  - flip a coin'
        '\n  - roll a die'
        '\n  - show a random xkcd comic'
        '\n  - latest news'
        '\n  - paradise lyrics'
        '\n  - ping google.com'
        '\n\nI\'m always learning, so do come back and say hi from time to time!'
        '\nHave a nice day. :)')

    message = TextTemplate(help).get_message()
    message = add_quick_reply(message, 'Tell me a joke', modules.generate_postback('joke'))
    message = add_quick_reply(message, 'Roll a die', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Latest News', modules.generate_postback('news'))
    message = add_quick_reply(message, 'Random xkcd comic', modules.generate_postback('xkcd'))

    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
