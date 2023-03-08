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

    # Command block
    if p_message[0] == '/':
        # Mention the author giving flowers to mention
        if p_message[1:6] == 'geliu':
            return_msg = f'{author.mention} dovanoja gėlių {p_message[7:]} 🌷🌷🌷'
            return return_msg
        # Send message that the beast mode has been enabled
        if p_message[1:6] == 'beast':
            return_msg = f'{author.mention} pajungia beast mode 👿.'
            return return_msg
        # Random number picker
        if p_message[1:5] == 'roll':
            match = re.search(r'^/roll\s\d+$', p_message)
            if match:
                random_number = random.randint(1, int(p_message[5:]))
                return_msg = f'{author.mention} your roll is **{random_number}**!'
            else:
                return_msg = f'Incorrect command usage. You typed: {p_message} \nCorrect usage example: "roll 100"'
            return return_msg

    # Help command
    if p_message == '!help':
        return """Currently implemented commands are:
                \n**/roll** (atsitiktinis skaičius tarp 1 ir kiek parašyta komandoje */roll 100*)
                \n**/beast** (pažadink savyje žvėrį)
                \n**/geliu** (padovanok kažkam gėlių */geliu @nickas*)
                \n**?(tavo žinutė)** (botas išsiūst žinutę privačiai.)"""
