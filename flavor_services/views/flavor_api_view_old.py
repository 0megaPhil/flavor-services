# from django.http import HttpResponse
# from llama import Tokenizer
# from llama.generation import LLaMA
# from llama_cpp import Llama
# from rest_framework.request import Request
# from rest_framework.views import APIView
#
# from flavor_services.entities.character import Character
# from flavor_services.entities.flavor import Flavor
# import torch
# import time
# import json
#
# model_location = r"X:\ml\models\Lexi-Llama-3-8B-Uncensored_F16.gguf"
#
# model = Llama(
#     model_path=model_location,
#     n_gpu_layers=-1,
#     device=torch.device('cuda'),
#     seed=53666,
#     n_ctx=4096,
#     embedding=True,
# )
#
# system_prompt = (r'''<<SYS>>You are a dungeon master running a role playing campaign,'
#                  ' do not break character, do not describe what you are about to do,'
#                  ' and then follow the coming prompts.<</SYS>>''')
#
#
# class FlavorCharacterApiView(APIView):
#     @staticmethod
#     def post(request: Request):
#         character = json.loads(str(request.body, encoding='utf-8'), object_hook=lambda d: Character(**d))
#         messages = get_flavor_messages(character)
#         output = get_flavor_output(messages)
#         flavor = Flavor(character.uuid, character.name, output)
#         print(flavor.to_json())
#         return HttpResponse(flavor.to_json())
#
#
# def get_flavor_messages(character: Character):
#     description = character.description
#     name = character.name
#     user_prompt = ('[INST]Use this player character  '
#                    'to help elaborate and describe this character as if describing them to a player\n'
#                    f'NAME: {name}\n'
#                    f'DESCRIPTION: {description}'
#                    'STATS: \n')
#     for stat in character.stats:
#         user_prompt += (f'\tSTAT_NAME: {stat.key}\n'
#                         f'\tSTAT_VALUE: {stat.value}\n'
#                         f'\tSTAT_DESCRIPTION: {stat.description}\n')
#     user_prompt += '[/INST]\n'
#     full_prompt = system_prompt + '\n' + user_prompt
#     print(full_prompt)
#     return full_prompt
#
#
# def get_flavor_output(messages):
#     try:
#         output = model(
#             f'Q:{messages}',
#             max_tokens=15,
#             stop=["Q:", "\n"],
#             echo=True
#         )
#         print(output)
#         return output
#     except Exception as e:
#         print(e)
#         return "ERROR: " + str(e)
#
#
# def load() -> LLaMA:
#     start_time = time.time()
#     print("Loading Tokenizer")
#     tokenizer = Tokenizer(model_location)
#     torch.set_default_tensor_type(torch.cuda.HalfTensor)
#     torch.set_default_tensor_type(torch.FloatTensor)
#     generator = LLaMA(model, tokenizer)
#     print(f"Loaded in {time.time() - start_time:.2f} seconds")
#     return generator
