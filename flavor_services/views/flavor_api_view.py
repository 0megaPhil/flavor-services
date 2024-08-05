import re

import jsonpickle
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.views import APIView

from flavor_services.entities.character import Character, CharacterStat, CharacterSkill
from flavor_services.entities.flavor import Flavor
import json

from flavor_services.generation import LlamaGeneration

system_prompt = r'''You are a dungeon master'''

generator = LlamaGeneration()


class FlavorCharacterApiView(APIView):
    @staticmethod
    def post(request: Request):
        body_str = str(request.body, encoding='utf-8')
        body_json = json.loads(body_str)
        print(body_json)
        character = Character(body_json)
        output = json.loads(get_flavor_output(character))
        flavor = Flavor(character.uuid, type(character), **output)
        print(flavor.to_json())
        return HttpResponse(flavor.to_json())


def get_message_list(character: Character):
    pickled_character = character.to_json()
    print(pickled_character)
    user_prompt = (f'For this Player Character: {pickled_character}, '
                   f'create a full description in json which has the following fields, '
                   f'appearance, background, personality and summary, in less than 512 characters')

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {"role": "user", "content": user_prompt},
    ]

    print("Chat Prompt: " + str(messages))
    return messages


def get_flavor_output(character: Character):
    try:
        messages = get_message_list(character)
        output = generator.generate_text(messages).split("<|start_header_id|>assistant<|end_header_id|>")[-1]
        output = output.replace("<|eot_id|>", "")
        print(output)
        found = output[output.find("{"):output.find("}") + 1]
        return found
    except Exception as e:
        print(e)
        return "ERROR: " + str(e)
