import sys
import json
import numpy as np



SYSTEM = """
You are a helpful assistant. 
You are always a reliable assistant that can answer questions with the help of external documents.
"""

'''
INSTRUCTIONS = """
- All contents between <DOCUMENTS> and </DOCUMENTS> are reference information retrieved from an external knowledge base.
- If you cannot answer based on the given information, you will return the sentence \"抱歉，检索到的参考信息并未提供充足的信息，因此无法回答。\".
- Please include the complete reference to the figure in your answer, "![figure](xxxx)" for example.

- Now, answer the following question based on the above retrieved documents:
{question}
- Return your answer in Markdown formatting, and in the same language as the question "{question}".
"""

'''

INSTRUCTIONS_PREV = """
- All contents between <DOCUMENTS> and </DOCUMENTS> are reference information retrieved from an external knowledge base.
- If you cannot answer based on the given information, you will return the sentence \"抱歉，检索到的参考信息并未提供充足的信息，因此无法回答。\".
- Now, answer the following question based on the following retrieved documents:
{question}
- Return your answer in Markdown formatting, and in Chinese".
"""
# No figure

INSTRUCTIONS_POST = """
- All contents between <DOCUMENTS> and </DOCUMENTS> are reference information retrieved from an external knowledge base.
- If you cannot answer based on the given information, you will return the sentence \"抱歉，检索到的参考信息并未提供充足的信息，因此无法回答。\".
- Now, answer the following question based on the above retrieved documents:
{question}
- Return your answer in Markdown formatting, and in Chinese".
"""


PROMPT_TEMPLATE = """
<SYSTEM>
{system}
</SYSTEM>

<USER_INSTRUCTIONS>
{user_instructions}
</USER_INSTRUCTIONS>

<INSTRUCTIONS>
{instructions_prev}
</INSTRUCTIONS>

<DOCUMENTS>
{context}
</DOCUMENTS>

<INSTRUCTIONS>
{instructions_post}
</INSTRUCTIONS>
"""


def construct_prompt(query : str, references: list, include_ref: bool = True):
    sep_s = sep_e = '\n'
    if include_ref:
        sep_s = '<reference>'
        sep_e = '</reference>'

    result_data = {
        'instruction': PROMPT_TEMPLATE.format(
            system=SYSTEM,
            instructions_prev=INSTRUCTIONS_PREV.format(question=query),
            user_instructions='',
            context=''.join(['\n'+sep_s + s + sep_e for s in references]),
            instructions_post=INSTRUCTIONS_POST.format(question=query)
        ),
        'input': '',
        'output': '',
        'history':[]
    } 
    
    return result_data


