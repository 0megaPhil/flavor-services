import threading

from flavor_services.generated.services_models import *
from flavor_services.generation import LlamaGeneration


class FlavorFactory:
    # Singleton
    generator: LlamaGeneration = LlamaGeneration()
    _char_dict: Dict[str, List[FeatureInput]] = {}
    id_threads: Dict[str, List[threading.Thread]] = {}
    entity_type: CommonObject

    def __init__(self, entity_type: CommonObject,
                 system_prompt=r'''You are a dungeon master in a grim dark setting''',
                 *args,
                 **kwargs):
        self.entity_type = entity_type
        self.entity_name = entity_type.get_flavor_type().replace("OTHER", entity_type.get_name())
        self.system_prompt = system_prompt
        self.args = args
        self.kwargs = kwargs
        self.features = [FeatureInput]

    def features(self):
        return self._char_dict[self.entity_name]

    def get_summary(self):
        char_json = schema_dumps(self.features)
        print(f"Details {char_json}")
        user_prompt = (f'For {self.entity_name} with features: {char_json}, '
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

    def complete_flavor(self, flavor_type: str, target_id: str):
        for feature in self.features:
            feature.target_id = target_id

        print(f"Generating Summary for {self.entity_name}")
        summary = self.generator.generate_string(self.get_summary())

        flavor: FlavorInput = FlavorInput()
        flavor.features = self.features
        flavor.type = flavor_type.upper()
        flavor.summary = summary
        flavor.target_id = target_id

        return flavor

    def _get_detail_prompt(self, entity: CommonObject):
        print(f"Class: {entity.__class__.__name__} - Prompt: {entity.prompt}")
        user_prompt = entity.prompt

        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {"role": "user", "content": f"Prompt: {user_prompt}"},
        ]

        print("Chat Prompt: " + str(messages))
        return messages

    def _generate_feature(self, entity: CommonObject):
        prompt = self._get_detail_prompt(entity)
        print(f"generate with {prompt}")
        output = self.generator.generate_json(prompt)
        for out in output:
            try:
                if ''"Prompt: "'' not in out:
                    feature = FeatureInput().from_json(out)
                    if hasattr(entity, "type"):
                        feature.type = entity.type
                    else:
                        feature.type = "OTHER"
                    if hasattr(entity, "context"):
                        feature.context = entity.context
                    else:
                        feature.context = "OTHER"
                    if hasattr(entity, "rarity"):
                        feature.rarity = entity.rarity
                    else:
                        feature.rarity = "OTHER"
                    if feature.title != "" and feature.description != "":
                        self.features.append(feature)
            except Exception as e:
                print(e)

    def _get_id_threads(self, target_id: str):
        if target_id not in self.id_threads.keys():
            print("No entities initialized")
            self.id_threads[target_id] = []
        return self.id_threads[target_id]

    def start_all(self, target_id: str):
        for thread in self._get_id_threads(target_id):
            print(f"Start Thread for: {target_id}")
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
            self._add_thread(target_id, entity)

    def _add_thread(self, target_id: str, entity: CommonObject):
        self._get_id_threads(target_id).append(
            threading.Thread(target=self._generate_feature,
                             args=(entity,)))
