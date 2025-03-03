import os

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


model_path = "models/deepseek/deepseek-llm-7b-chat"

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)

device = "mps" if torch.backends.mps.is_available() else "cpu"

model.to(device)


def generate_text(prompt, max_length: int, temperature: float, top_p=0.9, top_k=50):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_length=max_length, temperature=temperature)
    return tokenizer.decode(output[0], skip_special_tokens=True)


if __name__ == "__main__":
    prompt = "Say hello in Spanish"
    generated_text = generate_text(prompt)

    print(generated_text)
