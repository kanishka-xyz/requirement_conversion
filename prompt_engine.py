from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load Google FLAN-T5 model
model_name = "google/flan-t5-large"  # You can also try flan-t5-base or flan-t5-xl
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def convert_to_spec(requirement):
    prompt = (
        f"You are a software architect.\n"
        f"High-level requirement: {requirement}\n"
        f"Break it down into:\n"
        f"1. Modules (list the components/modules)\n"
        f"2. Database Schema (give table names and fields)\n"
        f"3. Pseudocode (basic logic for core features)\n"
        f"Provide the output in a clear and structured format."
    )

    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
    output_ids = model.generate(
        **inputs,
        max_length=1024,
        num_beams=4,
        temperature=0.7,
        do_sample=True
    )
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output
