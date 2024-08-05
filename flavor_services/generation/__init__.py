import timeit

import torch
import transformers
from datasets import Dataset
from tensorboard.compat import tf

from transformers import AutoModelForCausalLM, AutoTokenizer

TEXT_GENERATION = "text-generation"

torch.set_default_device('cuda:0')


class LlamaGeneration:
    max_length = 512
    model_name = r'F:\llm\Llama-3-8B-Lexi-Uncensored'
    cache_dir = f"./cache/{model_name}"

    @staticmethod
    def get_available_devices():
        physical_devices = tf.config.experimental.list_physical_devices('GPU')
        return str(physical_devices)

    def __init__(self):
        print("GPUs: " + str(tf.config.list_physical_devices('GPU')))
        print(self.get_available_devices())
        if not torch.cuda.is_available() or not tf.config.experimental.list_physical_devices('GPU'):
            raise Exception("No CUDA Available, physical GPU is not available")

        self.device = torch.device("cuda:0")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        start_time = timeit.default_timer()
        try:
            print(f"Assign Model with device: {self.device}")
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name,
                                                              local_files_only=True,
                                                              low_cpu_mem_usage=True,
                                                              torch_dtype=torch.float16,
                                                              cache_dir=self.cache_dir,
                                                              attn_implementation="flash_attention_2").to(self.device)
            self.model.generation_config.pad_token_id = self.tokenizer.pad_token_id
            elapsed = timeit.default_timer() - start_time
            print(f"Model assigned in time: {elapsed}")
        except Exception as e:
            print(f"Error: {e}")
            raise Exception("Failed to generate text-generation pipeline", e)

    def generate_text(self, messages):
        try:
            prompt = self.tokenizer.apply_chat_template(messages, tokenize=True,
                                                        add_generation_prompt=True, return_tensors="pt").to(self.device)

            outputs = self.model.to(self.device).generate(prompt, max_new_tokens=self.max_length,
                                                          pad_token_id=self.tokenizer.pad_token_id).to(self.device)
            print(self.tokenizer.decode(outputs[0]))
            return self.tokenizer.decode(outputs[0])
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"
