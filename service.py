import random

keywords = ['*you\'re', '*your', '*you are']

replies = ['annoying.', 'right.', 'a great person!', 'crazy!', 'funny!', 'really mean!'
           'not my mother!', 'a visionary', 'a tyrant', 'a little obsessed with grammar.']

def evaluate(comment):
    if (comment.lower() in keywords):
        return True
    return False


def get_reply():
    return replies[(random.randrange(0, len(
        replies)))] + '\n\n\n*I am a bot, don\'t take me seriously...* \n[source](https://github.com/scubar/correctionHunter)'
