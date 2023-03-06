import random
from typing import Any
import re

AVAILABLE_GREETINGS = ['labas', 'zdarova', 'sveikas', 'sveiki', 'privet', 'sw', 'swx', 'sw all', 'swx all',
                       'sveiki visi', 'laba', 'labs', 'laba diena', 'laba vakara', 'labas vakaras', 'hello', 'hi',
                       'sup', 'wassup', 'swsw']
AVAILABLE_GREETINGS_RESPONSES = ['Labas!', 'Laba!', 'Labuka', 'sw sw', 'swx']


def get_response(message: str, author: Any) -> str:
    """Generate a response to a pending request.

    :param message: original message send by a user.
    :param author: author of the original message.
    :return: response to request.
    """

    p_message = message.lower()

    # Respond with a greeting if user said hello
    if p_message in AVAILABLE_GREETINGS:
        response_msg = random.choice(AVAILABLE_GREETINGS_RESPONSES)
        return f'{author.mention} {response_msg}'

    # Random number picker method
    if p_message[:4] == 'roll':
        match = re.search(r'^roll\s\d+$', p_message)
        if match:
            random_number = random.randint(1, int(p_message[4:]))
            return_msg = f'{author.mention} your roll is **{random_number}**!'
        else:
            return_msg = f'Incorrect command usage. You typed: {p_message} \nCorrect usage example: "roll 100"'

        return return_msg

    # Help command
    if p_message == '!help':
        return '`Currently implemented commands are:' \
               '\n\t- roll (get a random number)' \
               '\n\t- hello (bot will say hello back)' \
               '\n\t- ?(your_text_here) to get a private message from the bot.`'
