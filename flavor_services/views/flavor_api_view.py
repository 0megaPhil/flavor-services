from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from flavor_services.entities.character import Character
from flavor_services.entities.flavor import Flavor
import json

from flavor_services.generation import LlamaGeneration

system_prompt = r'''You are a dungeon master'''

generator = LlamaGeneration()


class FlavorCharacterApiView(APIView):
    @staticmethod
    def post(request: Request):
        character = json.loads(str(request.body, encoding='utf-8'), object_hook=lambda d: Character(**d))
        output = get_flavor_output(character)
        flavor = Flavor(character.uuid, character.name, output)
        print(flavor.to_json())
        return HttpResponse(flavor.to_json())


def get_message_list(character: Character):
    description = character.description
    name = character.name
    user_prompt = ('Describe this character '
                   f'NAME: {name} '
                   f'DESCRIPTION: {description} '
                   'STATS: ')
    for stat in character.stats:
        user_prompt += (f'\tSTAT_NAME: {stat.key} '
                        f'\tSTAT_VALUE: {stat.value} '
                        f'\tSTAT_DESCRIPTION: {stat.description} ')

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {"role": "user", "content": user_prompt},
    ]

    print(messages)
    return messages


def get_sentence(character: Character):
    description = character.description
    name = character.name
    user_prompt = ('Use this information character to describe this character as if to a player'
                   f'NAME: {name} \n'
                   f'DESCRIPTION: {description} \n'
                   'STATS: \n')
    for stat in character.stats:
        user_prompt += (f'\tSTAT_NAME: {stat.key} \n'
                        f'\tSTAT_VALUE: {stat.value} \n'
                        f'\tSTAT_DESCRIPTION: {stat.description} \n')

    print(f"{system_prompt}, \n{user_prompt}")
    return f"{system_prompt}, \n{user_prompt}"


def get_flavor_output(character: Character):
    try:
        messages = get_message_list(character)
        output = generator.generate_text(messages)
        print(output)
        return output
    except Exception as e:
        print(e)
        return "ERROR: " + str(e)
