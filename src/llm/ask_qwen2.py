'''
Usage:

python ask_qwen2.py ../../data/test-query-ref.json  output_file

The first argument is the path to the datafile that  contains queries and their reference docs.
The second argument is the path to the output file.

'''

from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import sys
import pandas as pd
from tqdm import tqdm

from prompt import construct_prompt

model_path = '../../models/qwen2-7b-instruct/'
include_ref = True
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_path)


# test-query-ref.json
with open(sys.argv[1], 'r', encoding='utf-8') as fin:
    data = json.load(fin)

results = []
for item in tqdm(data):
    query = item['query']
    refs = item['references']
    prompt = construct_prompt(query, refs, include_ref=include_ref)
    messages = [
        {"role": "system", "content": prompt['instruction']},
        {"role": "user", "content": ''}
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    cur_dict = {'query' : query, 'references': refs, 'response': response }
    results.append(cur_dict)
    if (len(results)-1) % 10 == 0:
        print(f'query: {query}, response: {response}')
        print(f'prompt: {prompt}')

print(f'processed {len(results)} records.')
with open(sys.argv[2], 'w', encoding='utf-8') as fout:
    json.dump(results, fout, ensure_ascii=False, indent=4)
