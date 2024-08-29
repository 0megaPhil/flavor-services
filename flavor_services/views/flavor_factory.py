import threading
from typing import List, Dict

from flavor_services.generated_client import CharacteristicInput, FlavorInput
from flavor_services.generated_client.input_types import CommonObject, schema_dumps
from flavor_services.generation import LlamaGeneration


class FlavorFactory:
    # Singleton
    generator: LlamaGeneration = LlamaGeneration()
    _char_dict: Dict[str, List[CharacteristicInput]] = {}
    id_threads: Dict[str, List[threading.Thread]] = {}
    entity_type: CommonObject

    def __init__(self, entity_type: CommonObject,
                 system_prompt=r'''You are a dungeon master in a grim dark setting''',
                 *args,
                 **kwargs):
        self.entity_type = entity_type
        self.entity_name = entity_type.__class__.__name__.replace("Input", "")
        self.system_prompt = system_prompt
        self.args = args
        self.kwargs = kwargs
        self.characteristics = [CharacteristicInput]

    def characteristics(self):
        return self._char_dict[self.entity_name]

    def get_summary(self):
        char_json = schema_dumps(self.characteristics)
        print(f"Details {char_json}")
        user_prompt = (f'For {self.entity_name} with characteristics: {char_json}, '
                       f'create an interesting summary,'
                       f' as a string.'
                       f' Prefix generated string with <string> and suffix generated string with </string>')
        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {"role": "user", "content": user_prompt},
        ]
        print("Summary Prompt: " + str(messages))
        return messages

    def add_entity(self, target_id: str, entity: CommonObject):
        prompt = self._get_detail_prompt(entity)
        self._add_thread(target_id, prompt)

    def complete_flavor(self, target_id: str):
        for characteristic in self.characteristics:
            characteristic.target_id = target_id

        print(f"Generating Summary for {self.entity_name}")
        summary = self.generator.generate_string(self.get_summary())

        flavor: FlavorInput = FlavorInput()
        flavor.characteristics = self.characteristics
        flavor.type = self.entity_name
        flavor.summary = summary
        flavor.target_id = target_id

        return flavor

    def _get_detail_prompt(self, entity: CommonObject):
        additional = ""
        if hasattr(entity, "magnitude"):
            additional = f"Please note that this is {entity.magnitude} when compared to others. "
        if hasattr(entity, "rarity"):
            additional = f"Please note that rarity is {entity.rarity} when compared to others. "

        title = entity.get_title()
        obj_json = entity.__str__()
        print(f"Title: {title} - Detail {obj_json}")
        user_prompt = (f'Create an interesting description for "{self.entity_name}"'
                       f' with these details "{obj_json}", '
                       f' and return it as a json object of the following json format: '
                       '{'
                       '    "title": String,'
                       '    "description": String'
                       '}'
                       ' If there is a "type" field, include that in the "title"'
                       f' {additional}'
                       ' Prefix the generated json with <json> and suffix the generated json with </json>')

        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {"role": "user", "content": user_prompt},
        ]

        print("Chat Prompt: " + str(messages))
        return messages

    def _generate_characteristic(self, prompt: str):
        print(f"generate with {prompt}")
        output = self.generator.generate_json(prompt)
        for out in output:
            try:
                if ''"title"'' in out:
                    characteristic = CharacteristicInput().from_json(out)
                    if characteristic.title != "" and characteristic.description != "":
                        self.characteristics.append(characteristic)
            except Exception as e:
                print(e)

    def _get_id_threads(self, target_id: str):
        if target_id not in self.id_threads.keys():
            print("No entities initialized")
            self.id_threads[target_id] = []
        return self.id_threads[target_id]

    def start_all(self, target_id: str):
        for thread in self._get_id_threads(target_id):
            print(f"Start Thread for: {self.entity_name}")
            thread.start()

    def join_all(self, target_id: str):
        try:
            for thread in self._get_id_threads(target_id):
                print(f"Join Thread for: {self.entity_name}")
                self._get_id_threads(target_id).pop().join()
        finally:
            self.id_threads.pop(target_id, None)

    def initialize_all(self, target_id: str, entities: [CommonObject]):
        for entity in entities:
            prompt = self._get_detail_prompt(entity)
            self._add_thread(target_id, prompt)

    def _add_thread(self, target_id: str, prompt):
        self._get_id_threads(target_id).append(threading.Thread(target=self._generate_characteristic, args=(prompt,)))
