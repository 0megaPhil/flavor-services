from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM, AutoConfig, BertModel

from flavor_services.entities.character import Character
from flavor_services.entities.flavor import Flavor
import torch
import json

system_prompt = (r'''You are a dungeon master running a role playing campaign,'
                 ' do not break character, do not describe what you are about to do,'
                 ' and then follow the coming prompts.''')


class LlmPipe:
    model = None
    pipe = None
    tokenizer = None
    device = None

    def inputs(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors="pt").to(self.device)
        model = self.model.to(self.device)
        return model(inputs).to(self.device)

    def sequences(self, messages):
        return self.pipe(messages).to(self.device)

    def __init__(self):
        if self.model is None and self.pipe is None:
            if not torch.cuda.is_available():
                Exception("No CUDA Available")
            self.model_name = "./Llama-3-8B-Lexi-Uncensored"
            self.device = "cuda:0" if torch.cuda.is_available() else "cpu"

            print("Assign Tokenizer")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            print(f"Assign Model to Device: {self.device}, Please wait forever...")
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)
            print("Assign Pipeline")
            self.pipe = pipeline(model=self.model, tokenizer=self.tokenizer, device=self.device)


llm_pipe = LlmPipe()


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
    user_prompt = ('Use this player character  '
                   'to help elaborate and describe this character as if describing them to a player'
                   f'NAME: {name} \n'
                   f'DESCRIPTION: {description} \n'
                   'STATS: \n')
    for stat in character.stats:
        user_prompt += (f'\tSTAT_NAME: {stat.key} \n'
                        f'\tSTAT_VALUE: {stat.value} \n'
                        f'\tSTAT_DESCRIPTION: {stat.description} \n')
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    print(messages)
    return messages


def get_sentence(character: Character):
    description = character.description
    name = character.name
    user_prompt = ('Use this player character  '
                   'to help elaborate and describe this character as if describing them to a player'
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
        sentence = get_sentence(character)
        sentence_out = llm_pipe.inputs(sentence)
        print(sentence_out)
        sequences = llm_pipe.sequences(messages)
        print("Sequences" + str(sequences))
        output = ''
        for seq in sequences:
            print(f"Result: {seq['generated_text']}")
            output += seq['generated_text']

        print(output)
        return output
    except Exception as e:
        print(e)
        return "ERROR: " + str(e)
